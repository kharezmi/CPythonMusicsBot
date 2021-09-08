from django.contrib.auth.models import User
from django.db.models import fields
from .models import Users
from rest_framework import serializers

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['u_id', 'name']


