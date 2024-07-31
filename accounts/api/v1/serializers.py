from rest_framework import serializers
from accounts.models import CostumeUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class CostumeUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=250, write_only=True)

    class Meta:
        model = CostumeUser
        fields = ['email', 'password', 'confirm_password', 'is_active', 'is_admin']
        read_only_fields = ['is_active', 'is_admin']

    # hide password in get http method
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('password', None)
        return rep

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({'detail': "passwords doesn't match"})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return CostumeUser.objects.create_user(**validated_data)
