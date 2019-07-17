from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from account.models import AuthUser, Profile
from django.db import models

class AuthUserLoginForm(AuthenticationForm):
    
    class Meta(AuthenticationForm):
        model = AuthUser
        # fields = {'email', 'password'}

class AuthUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    password1 = forms.CharField(max_length=30, required=True)
    password2 = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    skype = forms.CharField(max_length=30, required=False)
    whatsapp = forms.CharField(max_length=30, required=False)
    twitter = forms.CharField(max_length=30, required=False)

    first_name.widget.attrs['class'] = 'form-control'
    # first_name.widget.attrs['placeholder'] = 'First Name'

    last_name.widget.attrs['class'] = 'form-control'
    # last_name.widget.attrs['placeholder'] = 'Last Name'

    password1.widget.attrs['class'] = 'form-control'
    password1.label = 'Password'
    # password1.widget.attrs['placeholder'] = 'Password'

    password2.widget.attrs['class'] = 'form-control'
    password2.label = 'Password Confirmation'
    # password2.widget.attrs['placeholder'] = 'Password Confirmation'

    email.widget.attrs['class'] = 'form-control'
    # email.widget.attrs['placeholder'] = 'Email'

    skype.widget.attrs['class'] = 'form-control'
    # skype.widget.attrs['placeholder'] = 'Skype'

    whatsapp.widget.attrs['class'] = 'form-control'
    # whatsapp.widget.attrs['placeholder'] = 'Whatsapp'

    twitter.widget.attrs['class'] = 'form-control'
    # twitter.widget.attrs['placeholder'] = 'Twitter'

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('first_name', 'last_name', 'password1', 'password2', 'email', 'skype', 'whatsapp', 'twitter')

class AuthUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = AuthUser
        fields = {'email'}

class AuthUserBuildRiskForm(UserCreationForm):
    max_spread = forms.IntegerField(required=False)
    size = forms.IntegerField(required=False)
    profit_limit = forms.IntegerField(required=False)
    stop_limit = forms.IntegerField(required=False)
    password1 = None
    password2 = None

    max_spread.widget.attrs['class'] = 'form-control'
    # first_name.widget.attrs['placeholder'] = 'First Name'

    size.widget.attrs['class'] = 'form-control'
    # last_name.widget.attrs['placeholder'] = 'Last Name'

    profit_limit.widget.attrs['class'] = 'form-control'
    # password1.widget.attrs['placeholder'] = 'Password'

    stop_limit.widget.attrs['class'] = 'form-control'
    # password2.widget.attrs['placeholder'] = 'Password Confirmation'

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('max_spread', 'size', 'profit_limit', 'stop_limit',)

class AuthUserPickProductForm(UserCreationForm):
    perdiction_accuracy = forms.IntegerField(required=False)
    price_charge_hight = forms.IntegerField(required=False)
    price_charge_low = forms.IntegerField(required=False)
    use_client_sentiment = forms.BooleanField(required=False)
    client_sentiment_contrarian = forms.BooleanField(required=False)
    client_sentiment_value = forms.CharField(required=False)
    watermark = forms.CharField(required=False)
    password1 = None
    password2 = None

    perdiction_accuracy.widget.attrs['class'] = 'form-control'
    price_charge_hight.widget.attrs['class'] = 'form-control'
    price_charge_low.widget.attrs['class'] = 'form-control'
    use_client_sentiment.widget.attrs['class'] = 'form-control'
    client_sentiment_contrarian.widget.attrs['class'] = 'form-control'
    client_sentiment_value.widget.attrs['class'] = 'form-control'
    watermark.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('perdiction_accuracy', 'price_charge_hight', 'price_charge_low', 'use_client_sentiment', 'client_sentiment_contrarian', 'client_sentiment_value', 'watermark')
