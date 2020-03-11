from django.db import models
from django.db.models import F
from cofferupApp.models import ContributorCoffer, TransactionType


class ContributorCofferTransaction(models.Model):

    contributor_coffer=models.ForeignKey(ContributorCoffer, on_delete=models.CASCADE)
    transaction_type=models.ForeignKey(TransactionType, on_delete=models.SET_NULL)
    is_contribution=models.BooleanField()
    description=models.CharField(max_length=255)
    amount=models.IntegerField()
    transaction_date=models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)
