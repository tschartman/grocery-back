from rest_framework import serializers
from visits.models import Visit

class VisitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = models.DateTimeField()
    store = models.CharField(max_length=100, blank=False)
    items = models.IntegerField()
    total = models.FloatField()
    location = models.CharField(max_length=100, blank=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.date = validated_data.get('date', instance.date)
        instance.store = validated_data.get('store', instance.store)
        instance.items = validated_data.get('items', instance.items)
        instance.total = validated_data.get('total', instance.total)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
