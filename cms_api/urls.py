from django.urls import path, include
from .views import LoginViewSet, RegisterAPI, ContentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('content', ContentViewSet, basename='content')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
]
