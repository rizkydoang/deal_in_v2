from rest_framework import serializers
from deal_in_v2.models import TblDocuments, TblUser, TblStore

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = TblDocuments
        fields = ('id', 'photo_store')


# class StoreSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = TblStore
#         fields = ('id','store', 'pin', 'nik', 'username')

#         def to_representation(self, instance):
#             self.fields['nik'] =  DocumentSerializer(read_only=True)
#             return super(DocumentSerializer, self).to_representation(instance)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = TblUser
        fields = ('username', 'password', 'name', 'address', 'birth_date', 'id_role', 'photo_profile')