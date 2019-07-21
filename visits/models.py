from django.db import models

# Create your models here.

class Visit(models.Model):
    date = models.DateTimeField()
    store = models.CharField(max_length=100, blank=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', related_name='visits', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)

class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    weight = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, related_name='items', on_delete=models.CASCADE)

