from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Headphone, Reviews


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ("headphone", "author", "review")


class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphone
        fields = ("id", "name", "description")
