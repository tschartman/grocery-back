from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from visits.models import Visit
from visits.models import Item
from visits.models import Store
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Store
        fields = ('url', 'id', 'name', 'domain', 'address', 'city', 'state', 'zipcode', 'owner')

class VisitSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    items = serializers.HyperlinkedRelatedField(many=True,  view_name='item-detail', read_only=True)

    class Meta:
        model = Visit
        fields = ('url', 'id', 'date', 'total', 'owner', 'items', 'store')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('url', 'id', 'name', 'brand', 'price', 'quantity', 'weight', 'owner', 'visit')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    visits = serializers.HyperlinkedRelatedField(many=True,  view_name='visit-detail', read_only=True)
    username = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            password = validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('url', 'id', 'password', 'first_name', 'last_name',  'username', 'visits')