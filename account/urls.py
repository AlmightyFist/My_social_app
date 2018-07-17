from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    #Widok logowania
    #url('login/',views.user_login, name='login'),
    path('',views.dashboard, name='dashboard'),
    path('login/', login,name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/',logout_then_login,name='logout_then_login'),
    path('password_change/', password_change, name='password_change'), #pozwala na zmiane hasła jeżeli użytkownik jest zalogowany
    path('password_change/done/', password_change_done, name = 'password_change_done'), #potwierdzenie pozytywnego przeprowadzenia operacji zmiany hasła
    path('password_reset/',password_reset, name='password_reset'),# 1 podanie maila połączonego z USER, który zapomniał hasła
    path('password_reset/done',password_reset_done, name='password_reset_done'), #2 potwierdzenie wysłania maila, wygenerowanie URL do resetowania hasła
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name='password_reset_confirm'), #3 wygenerowany automatycznie URL umożliwiający wprowadzenie nowego hasła
    path('password_reset/complete', password_reset_complete, name='password_reset_complete'), #4 potwierdzenie zmiany hasła, link do logowania
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    ]
