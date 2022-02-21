from rest_framework import serializers
from rest_framework.fields import empty
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Users
        fields = ('__all__')
class RelationsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Relations
        fields = ('__all__')
