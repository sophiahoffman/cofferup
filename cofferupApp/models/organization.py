# from django.db import models
# from django.db.models import F


# class Organization(models.Model):

#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=255)
#     date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

#     class Meta:
#         ordering = (F('name').asc(nulls_last=True),)
