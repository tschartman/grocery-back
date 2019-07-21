from rest_framework import serializers
from visits.models import Visit
from visits.models import Item
from django.contrib.auth.models import User


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    items = serializers.HyperlinkedRelatedField(many=True,  view_name='item-detail', read_only=True)

    class Meta:
        model = Visit
        fields = ('url', 'id', 'date', 'store', 'total', 'location', 'owner', 'items')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('url', 'id', 'name', 'brand', 'price', 'quantity', 'weight', 'owner', 'visit')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    visits = serializers.HyperlinkedRelatedField(many=True,  view_name='visit-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'visits')