from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from YouTravel.accounts.forms import LoginForm, RegisterForm, ProfileForm
from YouTravel.accounts.models import TravelProfile
from django.views.generic import ListView

from YouTravel.common.models import FriendRequest


def sign_in_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def sign_up_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile details')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def sign_out_user(request):
    logout(request)
    return redirect('index')


@login_required
def profile_details(request):
    profile = TravelProfile.objects.get(pk=request.user.id)
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/profile_details.html', context)


@login_required
def profile_edit(request):
    profile = TravelProfile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    context = {
            'form': form,
        }
    return render(request, 'accounts/edit_profile.html', context)


class TravelersListView(LoginRequiredMixin, ListView):
    model = TravelProfile
    template_name = 'accounts/profiles_list.html'
    paginate_by = 3

    def get_queryset(self):
        user_profile = TravelProfile.objects.get(user=self.request.user)
        return TravelProfile.objects.filter().exclude(friends=user_profile)


@login_required()
def send_friend_request(request, pk):
    from_user = TravelProfile.objects.get(user_id=request.user.id)
    to_user = TravelProfile.objects.get(user_id=pk)
    friend_request = FriendRequest(
        from_user=from_user,
        to_user=to_user)
    friend_request.save()

    return redirect('profiles list')


class ShowFriendRequests(LoginRequiredMixin, ListView):
    model = FriendRequest
    template_name = 'accounts/show_friend_requests.html'

    def get_queryset(self):
        user_profile = TravelProfile.objects.get(user=self.request.user)
        return FriendRequest.objects.filter(to_user=user_profile)


@login_required()
def accept_friend_request(request, pk):
    friends_request = FriendRequest.objects.get(id=pk)
    if friends_request.to_user == TravelProfile.objects.get(user_id=request.user.id):
        friends_request.to_user.friends.add(friends_request.from_user)
        friends_request.from_user.friends.add(friends_request.to_user)
        friends_request.delete()
    return render(request, 'accounts/request_list.html')


class ShowMyFriends(LoginRequiredMixin, ListView):
    model = TravelProfile
    template_name = 'accounts/friends_list.html'

    def get_queryset(self):
        user_profile = TravelProfile.objects.get(user=self.request.user)
        return TravelProfile.objects.filter(friends=user_profile)
