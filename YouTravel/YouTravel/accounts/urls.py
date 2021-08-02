from django.urls import path

from YouTravel.accounts.views import sign_in_user, sign_up_user, sign_out_user, profile_details, profile_edit, TravelersListView

urlpatterns = [
    path('sign_in/', sign_in_user, name='sign in'),
    path('sign_up/', sign_up_user, name='sign up'),
    path('sign_out/', sign_out_user, name='sign out'),
    path('profile/', profile_details, name='profile details'),
    path('profile_edit/', profile_edit, name='profile edit'),
    path('profiles/', TravelersListView.as_view(), name='profiles list'),

]
