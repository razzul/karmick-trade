from django.shortcuts import render
from django.http import HttpResponse
from account.forms import AuthUserLoginForm

# Create your views here.
def landing_page(request):
    form = AuthUserLoginForm()
    return render(request, 'landing/index.html', {'form': form})
    