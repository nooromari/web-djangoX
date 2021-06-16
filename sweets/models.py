from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    count = models.IntegerField()
    purchaser = models.ForeignKey(get_user_model(),on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])