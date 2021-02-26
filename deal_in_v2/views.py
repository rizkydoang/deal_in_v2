from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from deal_in_v2.models import TblUser 
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
                res.set_cookie(
                    'jwt', result[0]['jwt'], max_age=60*60*2)
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


def index(request):
    # if 'jwt' in request.COOKIES:
    #     jwt = JWTAuth()
    #     username = jwt.decode(request.COOKIES['jwt'])
    context = {
        # 'user': username['username']
        'title': 'Home | Deal In'
    }
    return render(request, 'content/index.html', context)
    # else:
    #     return render(request, 'content/index.html')