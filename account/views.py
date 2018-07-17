from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfilEditForm
from .models import Profile
from django.contrib import messages


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

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Utworzenie noweg oobiektu użytkownika, bez zapisywania jeszcze w bazie dostarczanych
            new_user = user_form.save(commit=False)
            #Ustawienie wybranego hasłas
            new_user.set_password(user_form.cleaned_data['password'])# metoda set_password modelu USER szyfrująca i zapisująca hasło
            #Zapisanie obiektu User
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

@login_required #wymagane uwierzytelnienie użytkownika przed wykonaniem widoku
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data=request.POST)
        profile_form = ProfilEditForm(instance = request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Uaktualnienie profilu zakończyło się sukcesem.')
        else:
            messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfilEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form': profile_form})
