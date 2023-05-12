from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from core.models import HeroSection, AboutSection
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, HeroSectionSerializer, AboutSectionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HeroSecitonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hero Section to be viewed or edited.
    """
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = []



class AboutSectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hero Section to be viewed or edited.
    """
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = []