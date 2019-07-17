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
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())
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
    max_spread = forms.FloatField(required=True)
    size = forms.FloatField(required=True)
    profit_limit = forms.FloatField(required=True)
    stop_limit = forms.FloatField(required=True)
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

# class AuthUserInvestmentForm(UserCreationForm):
    # currency1 = forms.ChoiceField(
    #     required=True, 
    #     choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')]
    # )
    #     currency_2 = forms.ChoiceField(required=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    #     currency_3 = forms.ChoiceField(required=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    #     currency_4 = forms.ChoiceField(required=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    #     currency_5 = forms.ChoiceField(required=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    #     currency_6 = forms.ChoiceField(required=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    #     password1 = None
    #     password2 = None

    #     # max_spread.widget.attrs['class'] = 'form-control'
    #     # # first_name.widget.attrs['placeholder'] = 'First Name'

    #     # size.widget.attrs['class'] = 'form-control'
    #     # # last_name.widget.attrs['placeholder'] = 'Last Name'

    #     # profit_limit.widget.attrs['class'] = 'form-control'
    #     # # password1.widget.attrs['placeholder'] = 'Password'

    #     # stop_limit.widget.attrs['class'] = 'form-control'
    #     # # password2.widget.attrs['placeholder'] = 'Password Confirmation'

    # class Meta(UserCreationForm):
    #     model = AuthUser
    #     fields = ('currency_1')

class AuthUserPickProductForm(UserCreationForm):
    product = forms.ChoiceField(choices=[('1', 'Invest IQ Premium Signals'), ('2', 'Invest IQ Automated Trading'), ('3', 'Invest IQ Managed Service')], widget=forms.RadioSelect)
    perdiction_accuracy = forms.FloatField(required=False)
    price_charge_hight = forms.FloatField(required=False)
    price_charge_low = forms.FloatField(required=False)
    use_client_sentiment = forms.ChoiceField(required=False, choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    client_sentiment_contrarian = forms.ChoiceField(required=False, choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    client_sentiment_value = forms.CharField(required=False)
    watermark = forms.CharField(required=False)
    password1 = None
    password2 = None

    product.widget.attrs['class'] = 'form-control'
    perdiction_accuracy.widget.attrs['class'] = 'form-control'
    price_charge_hight.widget.attrs['class'] = 'form-control'
    price_charge_low.widget.attrs['class'] = 'form-control'
    use_client_sentiment.widget.attrs['class'] = 'form-control'
    client_sentiment_contrarian.widget.attrs['class'] = 'form-control'
    client_sentiment_value.widget.attrs['class'] = 'form-control'
    watermark.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('product', 'perdiction_accuracy', 'price_charge_hight', 'price_charge_low', 'use_client_sentiment', 'client_sentiment_contrarian', 'client_sentiment_value', 'watermark')
