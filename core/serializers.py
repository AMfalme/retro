from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from .models import Snippet, HeroSection, AboutSection



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class HeroSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['title', 'paragraph', 'cta_text']


class AboutSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutSection
        fields = ['title', 'section', 'images']