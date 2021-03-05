from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from deal_in_v2.jwt import JWTAuth 
from deal_in_v2.models import TblUser, TblRole
# from deal_in_v2.models import * 
import requests
import json


# Create your views here.
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
        context = {
            'title': 'Home',
        }
        return render(request, 'content/index.html', context)

        
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
    res.delete_cookie('pin')
    res.delete_cookie('store')
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


def signup_store(request):
    if 'jwt' not in request.COOKIES:
        return redirect("home")
    else:
        if request.method == 'POST':
            jwt = JWTAuth()
            username = jwt.decode(request.COOKIES['jwt'])
            image = request.FILES['ktp_photo']
            data = {
                "id": request.POST['id'],
                "store": request.POST['store'],
                "username": username['username'],
                "documents": image.name,
                "nik": request.POST['nik'],
                "pin": request.POST['pin'],
            }
            response = requests.post('http://127.0.0.1:8000/api/auth/signup_store/'+username['username']+'/', json=data)
            result = []
            result.append(response.json())
            if result[0]['store'] != []:
                return redirect('pin_store_auth')
            else:
                messages.error(request, result[0]['message'])
                context = {
                    'title': 'Signup Store'
                }
                return render(request, 'login/signup_store.html', context)
        elif request.method == 'GET':
            jwt = JWTAuth()
            username = jwt.decode(request.COOKIES['jwt'])
            response = requests.get('http://127.0.0.1:8000/api/auth/signup_store/'+username['username']).json()
            result = []
            result.append(response)
            if result[0]['store'] != []:
                return redirect('pin_store_auth')
            else:
                messages.error(request, result[0]['message'])
                context = {
                    'title': 'Signup Store'
                }
                return render(request, 'login/signup_store.html', context)
        context = {
            'title': 'Signup Store'
        }
        return render(request, 'login/signup_store.html', context)


def signup_store_auth(request):
    if 'jwt' not in request.COOKIES:
        return redirect("home")
    else:
        if 'pin' in request.COOKIES:
            return redirect("index_store", id_store=request.COOKIES['store'])
        else:
            if request.method == 'POST':
                jwt = JWTAuth()
                username = jwt.decode(request.COOKIES['jwt'])
                pin = request.POST['pin']
                data = {
                    "username": username['username'],
                    "pin": pin
                }
                response = requests.post('http://127.0.0.1:8000/api/auth/signup_store_auth/', json=data)
                result = []
                result.append(response.json())
                if result[0]['store'] != []:
                    res = redirect("index_store", id_store=result[0]['store']['id'])
                    res.set_cookie('pin', result[0]['token'], max_age=60*60*2)
                    res.set_cookie('store', result[0]['store']['id'], max_age=60*60*2)
                    return res
                else:
                    messages.error(request, result[0]['message'])
                    context = {
                        'title': 'Store Auth'
                    }
                    return render(request, 'login/pin_store_auth.html', context)
            context = {
                'title': 'Store Auth'
            }
            return render(request, 'login/pin_store_auth.html', context)



def index_store(request, id_store):
    if 'jwt' not in request.COOKIES or 'pin' not in request.COOKIES:
        return redirect("home")
    else:
        jwt = JWTAuth()
        username = jwt.decode(request.COOKIES['jwt'])
        response = requests.get('http://127.0.0.1:8000/api/store/index_store/'+id_store).json()
        context = {
            'title': 'Home Store',
            'user': username['username'],
            'store': request.COOKIES['store'],
            'item_store': response
        }
        print(response)
        return render(request, 'store/index.html', context)


