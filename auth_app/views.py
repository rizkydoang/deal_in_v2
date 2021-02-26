import json
from django.shortcuts import render
from django.http import JsonResponse
from deal_in_v2.jwt import JWTAuth
from deal_in_v2.models import TblUser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']
        user = TblUser.objects.filter(username=username).values().first()
        if not user:
            return JsonResponse({"user": [], "message": "User tidak ditemukan !"}, status=400)

        if json_data['password'] != user['password']:
            return JsonResponse({"user": [], "message": "Username atau password anda salah !"}, status=400)

        jwt = JWTAuth()
        return JsonResponse({"user": user, "jwt": jwt.encode({"username": user['username']}), "message": "Berhasil Login"}, status=200)