from django.shortcuts import render
from .models import User, Profile , Permission
# Create your views here.reate/
def create(request):
    x=User(uname='seba',password='nada',mail='mail@mail.com',rut='12314123')
    x.save()
    return render(request, 'create.html')
