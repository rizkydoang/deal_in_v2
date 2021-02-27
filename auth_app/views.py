import json
from django.shortcuts import render
from django.http import JsonResponse
from deal_in_v2.jwt import JWTAuth
from deal_in_v2.models import TblUser, TblRole, TblStore
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


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user = TblUser()
            user.name = json_data['name']
            user.username = json_data['username']
            user.password = json_data['password']
            user.address = json_data['address']
            user.birth_date = json_data['birth_date']
            user.id_role = TblRole.objects.get(pk=json_data['id_role'])
            user.save()
            return JsonResponse({"user": list(TblUser.objects.filter(username=json_data['username']).values().first()), "message": "Akun Berhasil Terdaftar. Silahkan Login terlebih dahulu"}, status=200)
        except:
            return JsonResponse({"user": [], "message": "Isi data sesuai aturan!"}, status=200)


@csrf_exempt
def signup_store(request, username):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            if TblDocuments.objects.filter(pk=json_data['nik']).exists() or TblStore.objects.filter(pk=json_data['store']).exists():
                return JsonResponse({'store':[], "message": "Nama Toko atau NIK yang anda masukan sudah terdaftar"}, status=400)
            else:
                TblDocuments.objects.create(
                    id=json_data['nik'],
                    photo=json_data['documents']
                )
                TblStore.objects.create(
                    store=json_data['store'],
                    pin=json_data['pin'],
                    nik=TblDocuments.objects.get(pk=json_data['nik']),
                    username=TblUser.objects.get(pk=json_data['username'])
                )
                return JsonResponse({"store": list(TblStore.objects.filter(pk=json_data['store']).values().first()), "message": "Toko berhasil terdaftar"}, status=200)
        except:
            return JsonResponse({"store": [], "message": "Nama Toko atau NIK yang anda masukan sudah terdaftar"}, status=400)
    if request.method == 'GET':
        store = TblStore.objects.filter(username=username).values().first()
        if not store:
            return JsonResponse({"store": [], "message": "Anda perlu Daftar terlebih dahulu!"}, status=400)
        return JsonResponse({"store": list(store), "message": "Toko Berhasil Terdaftar"}, status=200)


@csrf_exempt
def signup_store_auth(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        store = TblStore.objects.filter(username=json_data['username']).first()
        if not store:
            return JsonResponse({"store": [], "message": "Anda perlu Daftar terlebih dahulu!"}, status=400)
        if store.pin == json_data['pin']:
            jwt = JWTAuth()
            store = TblStore.objects.filter(username=json_data['username']).values().first()
            return JsonResponse({"store": list(store), "token": jwt.encode({"pin": store['pin']}), "message": "Berhasil"}, status=200)
        else:
            return JsonResponse({"store": [], "message": "Pin Toko anda salah"}, status=400)