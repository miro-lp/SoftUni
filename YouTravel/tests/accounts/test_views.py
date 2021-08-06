from django.contrib.auth import get_user_model

from django.test import TestCase, Client
from django.urls import reverse, resolve

from YouTravel.accounts.models import TravelProfile
from YouTravel.common.models import FriendRequest

UserModel = get_user_model()


class AccountsViewsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.object.create_user(email='miro_lp@abv.bg', password='12345678')

    def test_login_GET(self):
        response = self.client.get(reverse('sign in'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_POST__user_exist(self):
        response = self.client.post(reverse('sign in'), data={
            'email': 'miro_lp@abv.bg',
            'password': '12345678'
        })

        self.assertEquals(response.status_code, 302)





    def test_login_POST__user_not_exist(self):
        user_1 = UserModel(id=2, email='miro_lp1@abv.bg', password='123456789')
        response = self.client.get(reverse('sign in'))
        with self.assertRaises(Exception) as ex:
            self.client.force_login(user_1)

        print(ex.exception)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_profile_details_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))
        profile = response.context['profile']

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.id, profile.user_id)
        self.assertTemplateUsed(response, 'accounts/profile_details.html')

    def test_profile_details_edit_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile edit'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_profile_details_edit_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('profile edit'), data={
            'first_name': 'Pesho'
        })
        self.assertEquals(response.status_code, 302)
        profile = TravelProfile.objects.get(user_id=self.user.id)
        self.assertEquals(profile.first_name, 'Pesho')

    def test_TravelersList_GET(self):
        self.client.force_login(self.user)
        user1 = UserModel.object.create_user(email='miro1_lp@abv.bg', password='123456781')

        response = self.client.get(reverse('profiles list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profiles_list.html')
        self.assertEquals(len(response.context['travelprofile_list']), 2)

    def test_send_friend_request(self):
        self.client.force_login(self.user)
        user1 = UserModel.object.create_user(email='miro1_lp@abv.bg', password='123456781')
        self.client.get(reverse('send friend request', kwargs={'pk': user1.id}))

        friends_request = FriendRequest.objects.all()
        self.assertEqual(len(friends_request), 1)

    def test_accept_friend_request(self):
        self.client.force_login(self.user)
        user1 = UserModel.object.create_user(email='miro1_lp@abv.bg', password='123456781')
        profile = TravelProfile.objects.get(user_id=self.user.id)
        profile1 = TravelProfile.objects.get(user_id=user1.id)
        FriendRequest.objects.create(from_user=profile1, to_user=profile)
        self.client.get(reverse('accept friend request', kwargs={'pk': self.user.id}))
        friends_request = FriendRequest.objects.all()
        self.assertEqual(len(friends_request), 0)

    def test_ShowFriendRequests_null_GET(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('show friend request'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/show_friend_requests.html')
        self.assertEquals(len(response.context['friendrequest_list']), 0)

    def test_ShowFriendRequests_not_null_GET(self):
        self.client.force_login(self.user)
        profile = TravelProfile.objects.get(user_id=self.user.id)
        user1 = UserModel.object.create_user(email='miro1_lp@abv.bg', password='123456781')
        profile1 = TravelProfile.objects.get(user_id=user1.id)

        friend_request = FriendRequest.objects.create(from_user=profile1, to_user=profile)

        response = self.client.get(reverse('show friend request'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/show_friend_requests.html')
        self.assertEquals(len(response.context['friendrequest_list']), 1)

    def test_ShowMyFriends_null_GET(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('friends list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/friends_list.html')
        self.assertEquals(len(response.context['travelprofile_list']), 0)

    def test_ShowMyFriends_not_null_GET(self):
        self.client.force_login(self.user)
        profile = TravelProfile.objects.get(user_id=self.user.id)
        user1 = UserModel.object.create_user(email='miro1_lp@abv.bg', password='123456781')
        profile1 = TravelProfile.objects.get(user_id=user1.id)
        profile1.friends.add(profile)
        profile.friends.add(profile1)

        response = self.client.get(reverse('friends list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/friends_list.html')
        self.assertEquals(len(response.context['travelprofile_list']), 1)
