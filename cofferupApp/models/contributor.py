from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Contributor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)
