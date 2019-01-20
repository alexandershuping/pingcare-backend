from django.contrib.auth.models import User, Group
from rest_framework import serializers

from backend.models import Ping

class UserSerializer(serializers.HyperlinkedModelSerializer):
	''' User APU representation '''
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class PingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ping
		fields = ('latitude', 'longitude', 'ping_count', 'issue', 'text_loc')
