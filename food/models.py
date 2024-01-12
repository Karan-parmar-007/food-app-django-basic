from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Items(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete= models.CASCADE, default = 1)
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.URLField(max_length=2000, default='https://images4.alphacoders.com/132/1325361.png')

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={'pk': self.pk})