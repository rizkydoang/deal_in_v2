from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# from deal_in_v2.middleware import jwtRequired
from deal_in_v2.models import *
from deal_in_v2.jwt import JWTAuth
import json
import requests
from pprint import pprint


def index_home(request):
    if request.method == 'GET':
        try:
            all_item = list(TblItem.objects.filter(deleted=0).values())

            for i in all_item:
                cat = TblCategory.objects.filter(id=i['id_category_id'], deleted=0).values().first()
                i.update({'id_category_id': cat})
            return JsonResponse({"all_item": all_item}, status=200)
        except:
            return JsonResponse({"all_item": []}, status=400)


def index_store(request, id_store):
    if request.method == 'GET':
        try:
            item_store = list(TblItem.objects.filter(id_store=id_store, deleted=0).values())

            for i in item_store:
                cat = TblCategory.objects.filter(id=i['id_category_id'], deleted=0).values().first()
                i.update({'id_category_id': cat})
            return JsonResponse({"item_store": item_store}, status=200)  
        except:
            return JsonResponse({"item_store": []}, status=400)


@csrf_exempt
def delete_item(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            TblItem.objects.filter(pk=json_data['id_item']).delete()
            return JsonResponse({"message": "Berhasil Menghapus Barang dari Toko"})
        except:
            return JsonResponse({"message": "Terjadi Error"})


@csrf_exempt
def update_item(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            TblItem.objects.filter(pk=json_data['id_item']).update(
                
            )
            return JsonResponse({"message": "Berhasil Menghapus Barang dari Toko"})
        except:
            return JsonResponse({"message": "Terjadi Error"})




