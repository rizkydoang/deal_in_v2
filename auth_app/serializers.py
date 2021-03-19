from rest_framework import serializers
from deal_in_v2.models import TblDocuments, TblUser, TblStore, TblItem

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = TblDocuments
        fields = ('id', 'photo_store')


class ItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = TblItem
        fields = ('name','quantity', 'id_category', 'id_store', 'description', 'photo_item', 'price')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = TblUser
        fields = ('username', 'password', 'name', 'address', 'birth_date', 'id_role', 'photo_profile')