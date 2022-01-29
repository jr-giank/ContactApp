from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    telephone_number = models.CharField(max_length=10, blank=False, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name + " " + self.last_name