from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from deal_in_v2.models import TblUser, TblRole
from deal_in_v2.jwt import JWTAuth 
# from deal_in_v2.models import * 
import requests


# Create your views here.
def login_user(request):
    if 'jwt' not in request.COOKIES:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            data = {"username": username, "password": password}
            response = requests.post('http://127.0.0.1:8000/api/auth/login/', json=data)
            result = []
            result.append(response.json())
            if result[0]['user'] != []:
                res = redirect("home")
                res.set_cookie('jwt', result[0]['jwt'], max_age=60*60*2)
                return res
            else:
                messages.error(request, result[0]['message'])
                return redirect("login_user")
    else:
        return redirect('home')
    context = {
        'title': 'Login Deal In'
    }
    return render(request, 'login/login.html', context)


def logout(request):
    res = redirect('login_user')
    res.delete_cookie('jwt')
    return res


def signup(request):
    if 'jwt' in request.COOKIES:
        return redirect("home")
    else:
        if request.method == 'POST':
            data = {
                "name": request.POST['name'],
                "username": request.POST['username'],
                "address": request.POST['address'],
                "birth_date": request.POST['birth_date'],
                "id_role": request.POST['role'],
                "password": request.POST['password']
            }
            response = requests.post('http://127.0.0.1:8000/api/auth/signup', json=data)
            result = []
            result.append(response.json())
            if result[0]['user'] != []:
                messages.error(request, result[0]['message'])
                return redirect('login_user')
            else:
                messages.error(request, result[0]['message'])
                return redirect('signup_user')
        context = {
            'title': 'Signup | DeaL.In'
        }
        return render(request, 'login/signup.html', context)


def index(request):
    if 'jwt' in request.COOKIES:
        jwt = JWTAuth()
        username = jwt.decode(request.COOKIES['jwt'])
        context = {
            'title': 'Home',
            'user': username['username']
        }
        return render(request, 'content/index.html', context)
    else:
        return render(request, 'content/index.html')