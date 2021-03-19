import json
from django.shortcuts import render
from django.http import JsonResponse
from deal_in_v2.jwt import JWTAuth
from deal_in_v2.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer, DocumentSerializer, ItemSerializer


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
        json_data = json.loads(request.body)
        try:
            TblUser.objects.create(
                name = json_data['name'],
                username = json_data['username'],
                password = json_data['password'],
                address = json_data['address'],
                birth_date = json_data['birth_date'],
                id_role = TblRole.objects.get(pk=json_data['id_role'])
            )
            return JsonResponse({"user": list(TblUser.objects.filter(username=json_data['username']).values().first()), "message": "Akun Berhasil Terdaftar. Silahkan Login terlebih dahulu"}, status=200)
        except:
            return JsonResponse({"user": [], "message": "Isi data sesuai aturan!"}, status=400)


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if request.data['side'] == 'profile':
            image_serializer = ProfileSerializer(data=request.data)
            if image_serializer.is_valid():
                image_serializer.save()
                return Response({'user': image_serializer.data, "message": "Akun Berhasil Terdaftar. Silahkan Login terlebih dahulu"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"user": []}, status=status.HTTP_400_BAD_REQUEST)
        elif request.data['side'] == 'store':
            image_serializer = DocumentSerializer(data=request.data)
            if not TblStore.objects.filter(store=request.data['store']).exists():
                if not TblStore.objects.filter(pk=request.data['id_store']).exists():
                    if image_serializer.is_valid():
                        image_serializer.save()
                        return Response({'store': image_serializer.data}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'store': [], "message": "NIK yang anda masukan sudah terdaftar"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'store': [], "message": "ID Toko yang anda masukan sudah terdaftar"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'store': [], "message": "Nama Toko yang anda masukan sudah terdaftar"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.data['side'] == 'item':
            image_serializer = ItemSerializer(data=request.data)
            if image_serializer.is_valid():
                image_serializer.save()
                return Response({'item': image_serializer.data, "message": "Barang berhasil ditambahkan"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"item": []}, status=status.HTTP_400_BAD_REQUEST)
 

@csrf_exempt
def signup_store(request, username):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            if TblDocuments.objects.filter(pk=json_data['nik']).exists():
                TblStore.objects.create(
                    id=json_data['id'],
                    store=json_data['store'],
                    pin=json_data['pin'],
                    nik=TblDocuments.objects.get(pk=json_data['nik']),
                    username=TblUser.objects.get(pk=json_data['username'])
                )
                return JsonResponse({"store": TblStore.objects.filter(store=json_data['store']).values().first(), "message": "Toko berhasil terdaftar"}, status=200)
            else:
                return JsonResponse({'store':[], "message": "Nama Toko atau ID Toko yang anda masukan sudah terdaftar"}, status=400)
        except:
            return JsonResponse({"store": [], "message": "Terjadi Error"}, status=400)
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
            return JsonResponse({"store": store, "token": jwt.encode({"pin": store['pin']}), "message": "Berhasil"}, status=200)
        else:
            return JsonResponse({"store": [], "message": "Pin Toko anda salah"}, status=400)



