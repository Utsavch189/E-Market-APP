from .views import *
from django.urls import path

urlpatterns = [
    path('jwt',jwt),
    path('createuser',createuser),
    path('sendotp',sendotp)
]