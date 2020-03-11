from django.db import models
from django.db.models import F
from cofferupApp.models import Contributor, Organization

class OrganizationContributor(models.Model):

    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)
