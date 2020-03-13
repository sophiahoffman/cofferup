# from django.db import models
from django.db.models import F
# from cofferupApp.models import Organization
from .contributor import Contributor
from django.db import models


class Coffer(models.Model):

    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    admin = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=255, null=True)

    # class Meta:
    #     ordering = (F('organization.name').asc(nulls_last=True),)

