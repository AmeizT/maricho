from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CharField
from apps.users.models import User, Account
from django import forms
from django.contrib.auth.hashers import check_password

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

        
class UserSerializer(serializers.ModelSerializer):
    password = CharField(
        style={'input_type': 'password'}
    )
    password2 = CharField(
        style={'input_type': 'password'},
        label="Confirm Password",
        write_only=True
    )
    account = AccountSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'surname',
            'username',
            'email',
            'password',
            'password2',
            'is_admin',
            'created',
            'account',
        )
        depth = 1
        lookup_field = 'username'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)
        user = User.objects.create_user(
            name=validated_data['name'],
            surname=validated_data['surname'],
            username=validated_data['surname'],
            email=validated_data['email'],
        )

        if password != password2:
            raise serializers.ValidationError('Passwords do not match please try again')
        elif len(password) < 8 or len(password2) < 8:
            raise serializers.ValidationError(
                'Password must contain at least 8 characters')
        else:
            user.set_password(password)
        user.save()
        return user
