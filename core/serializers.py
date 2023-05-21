from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from .models import Snippet, HeroSection, AboutSection, Studies, \
      WorkExperience, Projects, Technologies, SocialAccountLinks, ContactPage



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = '__all__'



class HeroSectionSerializer(serializers.ModelSerializer):
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


class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = '__all__'