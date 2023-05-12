from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


from django.urls import path, include
from .views import HeroSecitonViewSet, AboutSectionViewSet, StudiesViewSet, WorkExperienceViewSet, TechnologiesViewSet, SocialLinksViewSet, ProjectsViewSet

urlpatterns = [
    path('hero', HeroSecitonViewSet.as_view()),
    path('about', AboutSectionViewSet.as_view()),
    path('studies', StudiesViewSet.as_view()),
    path('work-experience', WorkExperienceViewSet.as_view()),
    path('technologies', TechnologiesViewSet.as_view()),
    path('social-links', SocialLinksViewSet.as_view()),
    

]