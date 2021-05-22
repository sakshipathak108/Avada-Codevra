from django.urls import path
from . import views


app_name = 'afterlogin'

urlpatterns = [
    path('contactus/', views.contact, name='contact'),
    path('join/', views.join, name='join'),
    path('join/<int:iidd>/', views.profile, name='profile'),
    path('find/', views.find, name='find'),
    path('join/<int:iidd>/test', views.addteammate, name='sendreq'),
    path('dashboard/events/', views.events, name="ev"),
    path('dashboard/events/<int:idev>', views.deletetheform, name="del"),
    path('dashboard/interested/', views.interested, name="interest"),
    path('join/search/', views.search, name="search"),
    path('join/searchbb/', views.searchbybranch, name="searchbb")

]
