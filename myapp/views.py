from django.shortcuts import render
from rest_framework import generics
from .models import Establishment
from .serializers import EstablishmentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from django_filters import rest_framework as filters

class EstablishmentList(generics.ListCreateAPIView):

    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Create your views here.
class EstablishmentNear(generics.ListCreateAPIView):

    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    #permission_classes = [IsAdminUser, TokenHasReadWriteScope]
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = '__all__'

    

class EstablishmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'