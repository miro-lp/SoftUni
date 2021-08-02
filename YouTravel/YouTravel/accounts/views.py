from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from YouTravel.accounts.forms import LoginForm, RegisterForm, ProfileForm
from YouTravel.accounts.models import TravelProfile
from django.views.generic import ListView

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


class TravelersListView(ListView):
    model = TravelProfile
    template_name = 'accounts/list_profiles.html'
