from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def contact(request):
    return render(request, 'generator/contact.html')


def password(request):
    chars = list('abcdefghjklmnopqrstuvwxyz')
    up_chars = list('ABCDEFGHJKLMNOPQRSTUVWXYZ')
    nums = list('0123456789')
    sp_chars = list('@#$%_!')
    length = int(request.GET.get('length', 12))
    pswd = ''
    if request.GET.get('uppercase'):
        chars.extend(up_chars)
    if request.GET.get('numbers'):
        chars.extend(nums)
    if request.GET.get('special'):
        chars.extend(sp_chars)
    random.shuffle(chars)
    for i in range(length):
        pswd += random.choice(chars)
    return render(request, 'generator/password.html', {'password': pswd})
