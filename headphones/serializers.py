from django.contrib.auth.models import User, Group
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from .models import Headphone, Reviews


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ "username"]

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self,obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('token', 'username', 'password')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CommentSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.author.username
    username = serializers.SerializerMethodField("get_username")

    class Meta:

        model = Reviews
        fields = ("headphone", "title","date","username", "author", "review", "price_rating")


class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphone
        fields = ("id", "name", "description", "impedance","frequency", "sensitivity")
