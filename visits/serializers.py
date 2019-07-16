from rest_framework import serializers
from visits.models import Visit
from django.contrib.auth.models import User

class VisitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Visit
        fields = ('id', 'date', 'store', 'items', 'total', 'location', 'owner')

class UserSerializer(serializers.ModelSerializer):
    visits = serializers.PrimaryKeyRelatedField(many=True, queryset=Visit.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'visits')