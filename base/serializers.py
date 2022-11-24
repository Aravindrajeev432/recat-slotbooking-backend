from rest_framework import serializers
# from users.models import Account
from django.contrib.auth.models import User
from .models import Application, Slots
from rest_framework.validators import UniqueValidator
import re


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # def validate(self,attrs):
    #
    #
    # def create(self, validated_data):
    #     user = Account.object.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         PhoneNumber=validated_data['phone']
    #
    #     )
    class Meta:
        model = User
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    userrs = serializers.CharField(source='user.username')

    class Meta:
        model = Application
        fields = '__all__'




class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = '__all__'

class ApprovedCompanies(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','answer1','company_name']
