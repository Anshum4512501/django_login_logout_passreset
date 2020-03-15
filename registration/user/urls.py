from django.urls import path
from . import views
urlpatterns= [
    path('signup/<id>',views.signup,name='user-signup'),
    # r'^time/plus/(\d{1,2})/$'
    # path(r'^time/plus/(\d{1,2})/$',views.signup,name='user-signup'),
    path('signup/',views.signup,name='user-signup'),
    
    path('signin/',views.signin,name='user-signin'),
    path('signinsuccess/',views.signinsuccess,name='user-signin-success'),
    path('forgetpassword/',views.forgetpassword,name='user-forget-password'),
    path('emailsuccess/',views.emailsuccess,name='user-email-success'),
    path('taskinfo/',views.taskinfo,name='user-task-info'),
    path('raiseticket/',views.ticketraising,name='user-ticket-raising'),
    path('assignticket/',views.assignticket,name='user-ticket-assign')
]