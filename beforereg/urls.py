from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('contactus/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='loginuser')
]
