from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.
""" #Widok logowania wygenerowany od podstaw bez wukorzystania domyślnych widoków dostarczanych przez Django
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username =cd['username'],# metoda ta zwraca obiekt klasy USER z atrybutami "username" i "password" lub NONE jeżeli dane nie zostaną uwierzytelnione
                                password=cd['password'])
            if user is not None:
                if user.is_active: # w przypadku pomyślnego uwierzytelnienia sprawdzamy czy konto jest aktywne - is_active to atrybut dostarczany przez Django
                    login(request, user) # jeżeli konto jest aktywne zostaje zalogowane w witrynie
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.') #jeżeli metoda authenticate zwróciła obiekt klasy USER
                else:
                    return HttpResponse('Konto jest zablokowane.')# jeżeli metoda authenticate zwróciła NONE
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniajace')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
"""
@login_required #dekorator sprawdza czy bieżący użytkownik został wierzytelniony. Jeżeli tak następuje wykonanie widoku. Jeżeli nie, zostaje przekierowany na stronę logowania a adres do, którego próbował sie dostać przekazywany jest jako parametr NEXT żądania GET
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dshboard'})
