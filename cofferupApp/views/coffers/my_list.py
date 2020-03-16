import sqlite3
from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def my_coffers_list(request, coffer_id=None):
    if request.method == 'GET':

        all_my_coffers = ContributorCoffer.objects.filter(contributor_id = request.user.id)
        my_paid_coffers = ContributorCofferTransaction.objects.filter(contributor_coffer_id__in=all_my_coffers, is_contribution=False)

        my_paid_coffers_list = []
        for coffer in my_paid_coffers:
            my_paid_coffers_list.append(coffer.contributor_coffer.coffer.id)
            print("paid coffer", coffer.contributor_coffer.coffer.id)


        all_my_coffers_list = []
        for coffer in all_my_coffers:
            all_my_coffers_list.append(coffer.coffer.id)
            print("my coffers", coffer.coffer.id)

        my_coffers = Coffer.objects.filter(id__in=all_my_coffers_list).exclude(id__in=my_paid_coffers_list)
        
        template = 'coffers/my_list.html'
        context = {
            'my_coffers': my_coffers
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a coffer from my coffers
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            contributor_coffer = ContributorCoffer.objects.get(coffer_id = coffer_id, contributor_id=request.user.id)
            contributor_coffer.delete()

            return redirect(reverse('cofferupApp:my_coffers'))    

        else:

            # instantiate...
            new_contributor_coffer = ContributorCoffer(
                coffer_id = coffer_id,
                contributor_id = request.user.id,
            )

            # and then save to the db
            new_contributor_coffer.save()

            return redirect(reverse('cofferupApp:my_coffers'))
