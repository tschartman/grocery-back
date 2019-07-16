from django.db import models

# Create your models here.

class Visit(models.Model):
    date = models.DateTimeField()
    store = models.CharField(max_length=100, blank=False)
    items = models.IntegerField()
    total = models.FloatField()
    location = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', related_name='visits', on_delete=models.CASCADE)


    class Meta:
        ordering = ('date',)