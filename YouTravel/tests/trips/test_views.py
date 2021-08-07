from django.contrib.auth import get_user_model

from django.test import TestCase, Client
from django.urls import reverse, resolve

from YouTravel.accounts.models import TravelProfile
from YouTravel.common.models import FriendRequest, Comment, Like
from YouTravel.trips.models import Continent, Trip

UserModel = get_user_model()


class AccountsViewsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.object.create_user(email='miro_lp@abv.bg', password='12345678')
        self.africa = Continent.objects.create(continent_name='Africa', description='Test',
                                               image='/medial_files/test.jpeg')

    def test_continents_listT_with_1_continent_GET(self):
        response = self.client.get(reverse('list continents'))

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'trips/continents_list.html')
        self.assertEquals(1, len(response.context['continent_list']))

    def test_trips_list_no_trips_GET(self):
        response = self.client.get(reverse('list trips', kwargs={'pk': self.africa.id}))

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'trips/list_trips.html')
        self.assertEquals(0, len(response.context['trips']))

    def test_trips_list_with_comment_like_GET(self):
        trip = Trip.objects.create(name_trip='Test_trip',
                                   country_name='Test_country',
                                   description='It is a test',
                                   continent=self.africa,
                                   user=self.user)
        Comment.objects.create(comment='Test comment',
                               user=self.user,
                               trip=trip)
        Like.objects.create(trip=trip,
                            user=self.user)

        response = self.client.get(reverse('list trips', kwargs={'pk': self.africa.id}))

        self.assertEquals(200, response.status_code, )
        self.assertTemplateUsed(response, 'trips/list_trips.html')
        self.assertEquals(1, len(response.context['trips']))
        self.assertEquals(1, len(response.context['comments']))
        self.assertTrue(response.context['is_liked_by_user'])

    def test_my_trips_list_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('my list trips'))

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'trips/my_list_trips.html')
        self.assertEquals(0, len(response.context['my_trips']))

    def test_add_trip_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add trip'))

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'trips/add_trip.html')

    def test_add_trip_invalid_form_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('add trip'), data={'name_trip': 'Test_trip',
                                                               'country_name': 'Test_country',
                                                               'description': 'It is a test',
                                                               'continent': 'Africa',
                                                               'image': '/tests/trips/test.jpeg'})

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'trips/add_trip.html')
