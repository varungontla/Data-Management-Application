from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# class Item(models.Model):
# Filename = models.CharField(max_length=100)
# File = models.FileField()

# def __str__(self):
#   return self.Filename


# class UploadItem(models.Model):
#   uploaditem = models.ForeignKey(Item, on_delete=models.CASCADE)
from django.db.models import ManyToManyField, ForeignKey


class Upload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    Filename = models.CharField(max_length=100)
    File = models.FileField()

    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Share(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    Sharing_File = models.FileField(Upload.File,blank=True)

    def __str__(self):
        return self.Sharing_File