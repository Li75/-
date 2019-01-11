from django.shortcuts import render

# Create your views here.
# import hashlib
from typing import Union

from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, response
from django.shortcuts import render, redirect


from sanfu.models import User


def index(request):
    return render(request,'index.html')


def regiest(request):
    if request.method == 'GET':
        return render(request,'regiest.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()
        response = redirect('sanfu:index')

        return response


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = request.objects.filter(username=username).filter(password=password)
        if users.count():
            response = redirect('sanfu:index')
            return response
        else:
            return render(request,'login.html')


def cart(request):
    return render(request,'cart.html')


def goodsMsg(request):
    if request.method == 'GET':
        return render(request,'goodsMsg.html')
    elif request.method == 'POST':
        response = redirect('sanfu:cart')
        return response


def goodsList(request):

    return render(request,'goodsList.html')