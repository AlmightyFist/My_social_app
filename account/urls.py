from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done

urlpatterns = [
    #Widok logowania
    #url('login/',views.user_login, name='login'),
    path('',views.dashboard, name='dashboard'),
    path('login/', login,name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/',logout_then_login,name='logout_then_login'),
    path('password_change/', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name = 'password_change_done'),
    ]
