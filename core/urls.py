from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


from django.urls import path, include
from .views import (
    HeroSectionListCreateViewSet,
    HeroSectionDetail,
    AboutSection, 
    StudiesViewSet,
    WorkExperienceViewSet, 
    TechnologiesViewSet, 
    SocialLinksViewSet, 
    ProjectsViewSet, 
    UserList, 
    UserDetail
)
from rest_framework import routers
router = routers.SimpleRouter()
# router.register(r'hero', HeroSectionListCreateViewSet)
# router.register(r'about', AboutSection)
router.register('social-links', SocialLinksViewSet),
router.register('studies', StudiesViewSet),
router.register('work-experience', WorkExperienceViewSet),
router.register('technologies', TechnologiesViewSet),

urlpatterns = [

    path('hero/', HeroSectionListCreateViewSet.as_view(), name="herosection"),
    path('herosection-detail/<int:pk>/', HeroSectionDetail.as_view()),
    path('users/', UserList.as_view(),),
    path('users/<int:pk>/', UserDetail.as_view(),name="user-detail"),
]

urlpatterns+=router.urls