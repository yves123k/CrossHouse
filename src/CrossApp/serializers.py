from numpy import TooHardError
from rest_framework import serializers
from .models import MyUser

class ModifyAdminSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = 'all'

class AdminListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = 'all'