from django.db.models import Sum
from cofferupApp.models import ContributorCofferTransaction, ContributorCoffer


def contributor_sum(coffer_id):
    """ contributor_sum generates a list of user first name, user last name and the total they have contributed to a specific coffer. list gets added to the coffer object later """
    # generates the list of ContributorCoffer objects based on the coffer_id from contributors function above
    contributors = ContributorCoffer.objects.filter(coffer_id = coffer_id)

    # for loop to populate a list of user first name, last name and total of their contributions to a specific coffer
    contributor_sums = []
    for c in contributors:

        cofferQuery = ContributorCofferTransaction.objects.filter(contributor_coffer = c).values('contributor_coffer').annotate(total=Sum('amount'))

        if len(cofferQuery) == 0:
            total = 0.0
        else:
            total = cofferQuery[0]['total']

        contributor_coffer_object = {
            "first_name": c.contributor.user.first_name,
            "last_name": c.contributor.user.last_name,
            "total": total/100
        }
        contributor_sums.append(contributor_coffer_object)

    return contributor_sums

def coffer_sum(coffer_id):
    """ coffer_sum generates a list of user first name, user last name and the total they have contributed to a specific coffer. list gets added to the coffer object in detail.py """

    coffer_sum = ContributorCofferTransaction.objects.filter(contributor_coffer__coffer_id = coffer_id).aggregate(Sum('amount'))['amount__sum']

    if coffer_sum is None:
        coffer_sum=0.0
    else:
        coffer_sum = coffer_sum/100
    return coffer_sum