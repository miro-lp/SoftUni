from django.test import SimpleTestCase
from django.urls import reverse, resolve
from YouTravel.accounts.views import *


class TestUrls(SimpleTestCase):

    def test_sign_in_url(self):
        url = reverse('sign in')
        self.assertEqual(resolve(url).func, sign_in_user)

    def test_sign_up_url(self):
        url = reverse('sign up')
        self.assertEqual(resolve(url).func, sign_up_user)

    def test_sign_out_url(self):
        url = reverse('sign out')
        self.assertEqual(resolve(url).func, sign_out_user)

    def test_sign_out_url(self):
        url = reverse('profile details')
        self.assertEqual(resolve(url).func.view_class, ProfileDetails)

    def test_profile_edit(self):
        url = reverse('profile edit')
        self.assertEqual(resolve(url).func, profile_edit)

    def test_profile_edit(self):
        url = reverse('profiles list')
        self.assertEqual(resolve(url).func.view_class, TravelersListView)

    def test_send_friend_request(self):
        url = reverse('send friend request', kwargs={'pk': int()})
        self.assertEqual(resolve(url).func, send_friend_request)

    def test_show_friend_request(self):
        url = reverse('show friend request')
        self.assertEqual(resolve(url).func.view_class, ShowFriendRequests)

    def test_accept_friend_request(self):
        url = reverse('accept friend request', kwargs={'pk': int()})
        self.assertEqual(resolve(url).func, accept_friend_request)

    def test_show_friends(self):
        url = reverse('friends list')
        self.assertEqual(resolve(url).func.view_class, ShowMyFriends)




