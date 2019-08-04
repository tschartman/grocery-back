from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100, blank=False)
    domain = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, blank=False)
    owner = models.ForeignKey('auth.User', related_name='stores', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

class Visit(models.Model):
    date = models.DateTimeField(blank=False)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    owner = models.ForeignKey('auth.User', related_name='visits', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='visits', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)

class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False)
    weight = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, related_name='items', on_delete=models.CASCADE)

