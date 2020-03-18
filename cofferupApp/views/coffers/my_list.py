from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def my_coffers_list(request, coffer_id=None):
    if request.method == 'GET':

        my_open_coffers = ContributorCoffer.objects.filter(contributor_id=request.user.id, is_settled=False, coffer__date_end__gte=date.today())
        my_closed_coffers = ContributorCoffer.objects.filter(contributor_id=request.user.id, is_settled=False, coffer__date_end__lt=date.today())

        template = 'coffers/my_list.html'
        context = {
            'my_open_coffers': my_open_coffers,
            'my_closed_coffers': my_closed_coffers
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
