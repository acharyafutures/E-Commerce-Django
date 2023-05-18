from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural= 'Categories'
        ordering=('name',)
    
    def __str__(self):
        return(self.name)


class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description= models.TextField(blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    price=models.FloatField(default=0)
    image=models.ImageField(upload_to='item_images', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return(self.name)