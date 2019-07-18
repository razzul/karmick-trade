from django.contrib.auth import login as core_login, logout as core_logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.forms import AuthUserCreationForm, AuthUserChangeForm, AuthUserLoginForm, AuthUserBuildRiskForm, AuthUserPickProductForm
from django.contrib.auth.decorators import login_required
from account.models import AuthUser, Profile
import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import get_template
from django.template import Context

from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def login(request):
    
    if request.method == 'POST':
        form = AuthUserLoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    core_login(request, user)
                    return redirect('dashboard')
    else:
        form = AuthUserLoginForm()

    return render(request, 'auth/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = AuthUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.skype = form.cleaned_data.get('skype')
            user.profile.whatsapp = form.cleaned_data.get('whatsapp')
            user.profile.twitter = form.cleaned_data.get('twitter')
            user.save()

            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            core_login(request, user)
            # email
            res = send_mail("hello paul", "test", "rajul@karmicksolutions.com", [username])
            messages.add_message(request, messages.INFO, res)

            return redirect('build_risk_pro')
    else:
        form = AuthUserCreationForm()
    
    return render(request, 'auth/signup.html', {'form': form})

def logout(request):
    pass

@login_required
def build_risk_pro(request):
    if request.method == 'POST':
        form = AuthUserBuildRiskForm(request.POST)

        if form.is_valid():
            user = request.user
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.max_spread = form.cleaned_data.get('max_spread')
            user.profile.size = form.cleaned_data.get('size')
            user.profile.profit_limit = form.cleaned_data.get('profit_limit')
            user.profile.stop_limit = form.cleaned_data.get('stop_limit')
            user.save()

            return redirect('pick_product')
    else:
        user = request.user
        data = {'max_spread': user.profile.max_spread, 'size': user.profile.size, 'profit_limit': user.profile.profit_limit, 'stop_limit': user.profile.stop_limit}
        form = AuthUserBuildRiskForm(initial=data)

    return render(request, 'auth/build_risk_pro.html', {'form': form})

@login_required
def pick_product(request):
    if request.method == 'POST':
        form = AuthUserPickProductForm(request.POST)

        if form.is_valid():
            user = request.user
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.product = form.cleaned_data.get('product')
            if (user.profile.product != '3'):
                user.profile.perdiction_accuracy = form.cleaned_data.get('perdiction_accuracy')
                user.profile.price_charge_hight = form.cleaned_data.get('price_charge_hight')
                user.profile.price_charge_low = form.cleaned_data.get('price_charge_low')
                user.profile.use_client_sentiment = form.cleaned_data.get('use_client_sentiment')
                user.profile.client_sentiment_contrarian = form.cleaned_data.get('client_sentiment_contrarian')
                user.profile.client_sentiment_value = form.cleaned_data.get('client_sentiment_value')
                user.profile.watermark = form.cleaned_data.get('watermark')
            else:
                user.profile.perdiction_accuracy = '0'
                user.profile.price_charge_hight = '0'
                user.profile.price_charge_low = '0'
                user.profile.use_client_sentiment = 'no'
                user.profile.client_sentiment_contrarian = 'no'
                user.profile.client_sentiment_value = ''
                user.profile.watermark = ''
            user.save()

            return redirect('review')
    else:
        # user = request.user
        # data = {'product': user.profile.product,'perdiction_accuracy': user.profile.perdiction_accuracy, 'price_charge_hight': user.profile.price_charge_hight, 'price_charge_low': user.profile.price_charge_low, 'use_client_sentiment': user.profile.use_client_sentiment, 'client_sentiment_contrarian': user.profile.client_sentiment_contrarian, 'client_sentiment_value': user.profile.client_sentiment_value, 'watermark': user.profile.watermark}
        form = AuthUserPickProductForm()

    return render(request, 'auth/pick_product.html', {'form': form})

@login_required
def review(request):
    return render(request, 'auth/review.html', {})

@login_required
def run(request):
    return render(request, 'auth/run.html', {})

def email(request, email_id):
    user = request.user

    html_message = render_to_string('auth/account_activation_email.html', {'user': user})
    res = send_mail("Welcome to Karmick Trade", '', "rajul@karmicksolutions.com", [email_id], html_message=html_message)
    # return HttpResponse('%s'%res)
    messages.add_message(request, messages.INFO, res)
    return redirect('build_risk_pro')
