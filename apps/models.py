from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="gallery",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    village = models.CharField(max_length=40, null=True)
    province = models.CharField(max_length=40, null=True)
    district = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    image = models.ImageField(upload_to="gallery", blank=True)
    def __str__(self) -> str:
        return self.user.username