from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ContentSerializer
from .models import ContentModel
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Viewset that checks login credentials and returns token
class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

# APIView for User Registration
class RegisterAPI(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user).key
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token":token
        })

# Filter for Contents
class ContentFilter(filters.FilterSet):

	class Meta:
		model = ContentModel
		fields = {
		'title':['icontains'],
		'body':['icontains'],
		'summary':['icontains'],
		'categories':['icontains']
		}

# ModelViewSet to handle CRUD operations of Content Model
class ContentViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = ContentSerializer
    
    # Allow Access only if user is Authenticated
    permission_classes = (IsAuthenticated,)
    
    # Intitialize Filter
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContentFilter

    # If current user is not admin, give user only his content. If admin, give all content 
    def get_queryset(self):
    	user = self.request.user
    	if user.is_superuser:
    		return ContentModel.objects.all()
    	else:
    		return ContentModel.objects.filter(author=self.request.user.id)

    # Used to assign foreign key user from User model to author in Content Model
    def perform_create(self, serializer):
    	serializer.save(author=self.request.user)