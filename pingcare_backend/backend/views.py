from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from backend.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	''' API endpoint to view/edit users '''
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	''' API endpoint to view/edit groups '''
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

# Create your views here.
def index(request):
	return HttpResponse('Hello swamphacks')
