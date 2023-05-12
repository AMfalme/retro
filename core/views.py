from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from core.models import HeroSection, AboutSection, Studies, WorkExperience, Technologies, Projects, SocialAccountLinks
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, HeroSectionSerializer, AboutSectionSerializer, StudiesSeializer, ProjectsSerializer, WorkExperienceSerializer, TechnologiesSerializer, SocialLinksSerializer
from django.http import HttpResponse

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
    permission_classes = [permissions.IsAuthenticated]



class AboutSectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hero Section to be viewed or edited.
    """
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudiesViewSet(viewsets.ModelViewSet):
    queryset = Studies.objects.all()
    serializer_class = StudiesSeializer
    permission_classes = [permissions.IsAuthenticated]


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

class TechnologiesViewSet(viewsets.ModelViewSet):
    queryset = Technologies.objects.all()
    serializer_class = TechnologiesSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialAccountLinks.objects.all()
    serializer_class = SocialLinksSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated]