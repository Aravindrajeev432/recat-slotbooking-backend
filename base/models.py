from django.db import models
# from users.models import Account
from django.contrib.auth.models import User


# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    company_name = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    answer1 = models.TextField(max_length=500, default="")
    answer2 = models.TextField(max_length=500, default="")
    answer3 = models.TextField(max_length=500, default="")
    answer4 = models.TextField(max_length=500, default="")
    answer5 = models.TextField(max_length=500, default="")
    answer6 = models.TextField(max_length=500, default="")
    proposal = models.CharField(max_length=50, default="")
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

    applied = models.BooleanField(default=True)
    Denied = models.BooleanField(default=False)
    Approved = models.BooleanField(default=False)
    alloted = models.BooleanField(default=False)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Slots(models.Model):
    user = models.IntegerField(blank=True, null=True)
    application = models.IntegerField(blank=True, null=True, unique=True)
    company_name = models.CharField(max_length=50,null=True)


