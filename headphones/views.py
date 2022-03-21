
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .models import Headphone, Reviews
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    GroupSerializer,
    HeadphoneSerializer,
    CommentSerializer,
)
        
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HeadphoneView(viewsets.ModelViewSet):
    serializer_class = HeadphoneSerializer
    queryset = Headphone.objects.all()


class ReviewView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Reviews.objects.all()
