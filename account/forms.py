from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','email')

    def clean_password2(self): #metoda clean może zostać dostarczona dla dowolnego pola formularza w celu wyczyszczenia jego wartości lub zgłoszczenia błędu weryfikacji
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return cd['password2']

class UserEditForm(forms.ModelForm): #edycja kolumn przechowywanych we wbudowanym modelu User
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfilEditForm(forms.ModelForm): #edycja danych dodatkowcyh przechowywanych w modelu Profile
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')
