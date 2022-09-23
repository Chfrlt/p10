from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework_simplejwt import views as jwt_views

from project.views import ProjectViewSet
from contributors.views import ContributorViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet
from users.views import RegisterAPIView


router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

project_router = NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'users', ContributorViewSet, basename='users')
project_router.register(r'issues', IssueViewSet, basename='issues')

issue_router = NestedSimpleRouter(project_router, r'issues', lookup='issues')
issue_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('signup/', RegisterAPIView.as_view()),
    path(
        'login/', jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
        ),
    path(
        'api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
        ),
]
