from rest_framework import serializers

from .models import *

class OwnerSerializer(serializers.ModelSerializer):
    '''
    顧客驗證
    '''
    class Meta:
        model = Owner
        fields = ('__all__')

class PetSerializer(serializers.ModelSerializer):
    birthday = serializers.CharField(source="pet.birth_date")
    '''
    寵物驗證
    '''
    class Meta:
        model = Pet
        fields = ('name', 'nickname', 'gender', 'birth_date', 'birth_date')

# class PetWithOwnerSerializer(serializers.ModelSerializer):

#     class OwnerSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Owner
#             fields = ('__all__')
    
#     owner = OwnerSerializer()

#     class Meta:
#         model = Pet
#         fields = '__all__' #TODO