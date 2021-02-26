from django.shortcuts import render
from django.http import JsonResponse
from deal_in_v2.models import TblUser 

# Create your views here.
def detail(request, id):
    if request.method == 'GET':
        if id == 'all':
            user = list(TblUser.objects.all().values())
            return JsonResponse({'user': user})
        else:
            user = TblUser.objects.filter(username=id).values().first()
            if not user:
                return JsonResponse({'message': 'Pengguna Tidak ditemukan!'}, status=400)
            return JsonResponse({'user': [user]}, status=200)