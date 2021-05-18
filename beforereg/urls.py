from django.urls import path
from beforereg import views


urlpatterns = [
    path('home/', views.index, name='index'),
    path('contactus/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='loginuser'),
    path('dashboard/', views.afterlogindash, name='dashboard'),
    path('', views.logout_user, name='logoutuser'),

]
