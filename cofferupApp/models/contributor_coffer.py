from django.db import models
from django.db.models import F
from .contributor import Contributor
from .coffer import Coffer

class ContributorCoffer(models.Model):

    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    coffer = models.ForeignKey(Coffer, on_delete=models.CASCADE)
    # is_open=models.BooleanField(default=True)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)
