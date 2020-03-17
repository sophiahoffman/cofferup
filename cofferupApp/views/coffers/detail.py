import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from ..helpers import contributor_sum, coffer_sum

def get_coffer(coffer_id):
    return Coffer.objects.get(pk = coffer_id)

@login_required
def coffer_detail(request, coffer_id):
    if request.method == 'GET': 
        
        coffer = get_coffer(coffer_id)
        coffer.sum = coffer_sum(coffer_id)
        coffer.contributor_sums = contributor_sum(coffer_id)

        # contributor_coffer = ContributorCoffer.objects.get(coffer_id=coffer_id)
        # contributor_coffer_transactions = ContributorCofferTransaction.objects.filter(contributor_coffer_id=contributor_coffer.id, )        


        template = 'coffers/detail.html'
        context = {'coffer': coffer}

        return render(request, template, context)

    elif request.method == 'POST':
        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            coffer = Coffer.objects.get(coffer_id = coffer_id)
            coffer.delete()

            return redirect(reverse('cofferupApp:coffers')) 