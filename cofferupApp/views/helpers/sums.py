from django.db.models import Sum
from cofferupApp.models import ContributorCofferTransaction, ContributorCoffer


def contributor_sum(coffer_id):
    """ contributor_sum generates a list of user first name, user last name and the total they have contributed to a specific coffer. list gets added to the coffer object later 
    accomplishes left join and an equivalent to the following SQL query:
    select t1.first_name, t1.last_name, t1.contributor_coffer, t1.contributor_id, t1.coffer_id, t2.total
    from
    (select au.first_name as first_name, au.last_name as last_name, cc.id as contributor_coffer, cc.contributor_id as contributor_id, cc.coffer_id as coffer_id
    from auth_user au
    join cofferupApp_contributorcoffer cc
    on au.id = cc.contributor_id) as t1
    left join
    (select cct.contributor_coffer_id as contributor_coffer, sum(amount) as total
    from cofferupApp_contributorcoffertransaction cct
    group by cct.contributor_coffer_id) as t2
    on t1.contributor_coffer = t2.contributor_coffer
    order by coffer_id, total DESC; 
    """
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
            "image_url": c.contributor.image_url,
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