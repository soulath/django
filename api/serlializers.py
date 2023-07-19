from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'category', 'subcatgeory', 'name', 'amount')


class UserSerializer(serializers.ModelSerializer):
	class Meta (object):
		model = User
		fields = ['id', 'username', 'password', 'email']