from django.urls import path
from . import views
from .models import findform


app_name = 'afterlogin'

urlpatterns = [
    path('contactus/', views.contact, name='contact'),
    path('join/', views.join, name='join'),
    path('join/<int:iidd>/', views.profile, name='profile'),
    path('find/', views.find, name='find'),
]
