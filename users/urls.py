from django.urls import path
from django.conf.urls import url, patterns
from .views import UserView, authenticate_user


app_name = "users"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('users/', UserView.as_view())
    path('login/', authenticate_user)
]
