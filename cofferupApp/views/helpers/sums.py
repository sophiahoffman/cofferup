from django.db.models import Sum
from cofferupApp.models import ContributorCofferTransaction, ContributorCoffer



def contributor_sum(coffer_id):
    # contributors = ContributorCoffer.objects.filter(coffer_id=coffer_id)
    transactions = ContributorCofferTransaction.objects.filter(contributor_coffer__coffer_id = coffer_id).values('contributor_coffer').annotate(total = Sum('amount')).order_by('-total')

    contributor_sums = []
    for item in transactions:
        index = item['contributor_coffer']
        contributor_coffer = ContributorCoffer.objects.get(pk=index)
        contributor_coffer_object = {
            "first_name": contributor_coffer.contributor.user.first_name,
            "last_name": contributor_coffer.contributor.user.last_name,
            "total": item['total']/100
        }
        contributor_sums.append(contributor_coffer_object)
    
    return contributor_sums

def coffer_sum(coffer_id):
    coffer_sum = ContributorCofferTransaction.objects.filter(contributor_coffer__coffer_id = coffer_id).aggregate(Sum('amount'))['amount__sum']

    if coffer_sum is None:
        coffer_sum=0
    else:
        coffer_sum = coffer_sum/100
    return coffer_sum