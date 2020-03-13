from django.urls import path
from . import views
urlpatterns= [
    path('signup/',views.signup,name='user-signup'),
    path('signin/',views.signin,name='user-signin'),
    path('signinsuccess/',views.signinsuccess,name='user-signin-success'),
    path('forgetpassword/',views.forgetpassword,name='user-forget-password'),
]