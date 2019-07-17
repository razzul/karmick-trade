from django.shortcuts import render
from django.http import HttpResponse
from account.models import AuthUser

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html', {})

def user_list(request):
    users = AuthUser.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})