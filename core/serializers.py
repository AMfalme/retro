from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from .models import Snippet, HeroSection, AboutSection, Studies, WorkExperience, Projects, Technologies, SocialAccountLinks



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
        fields = '__all__'


class AboutSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'

class StudiesSeializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studies
        fields = '__all__'

class WorkExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class TechnologiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SocialLinksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialAccountLinks
        fields = '__all__'