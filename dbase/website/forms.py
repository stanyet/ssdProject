from django import forms
from django.contrib.auth.models import User
from django.db import models



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    SEX = [
        ("M","Male"),
        ("F","Female")
    ]
    BIRTH_YEAR_CHOICES = range(1970,2018)

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    gender = forms.ChoiceField(label='Gender', choices=SEX)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = User
        #From User fields
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean_password2(self):
        '''Check if both password matches'''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
