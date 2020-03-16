from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def my_settled_coffers_list(request):
    if request.method == 'GET':

        """ settled coffers are coffers that are paid by an individual.
        filters contributor coffer join so only those with contributor id matching the logged in user are returned; then uses that filter on contributor coffer transaction to get only those that are paid"""

        my_coffers = ContributorCoffer.objects.filter(contributor_id=request.user.id )
        my_paid_coffers = ContributorCofferTransaction.objects.filter(contributor_coffer_id__in=my_coffers, is_contribution=False)

        template = 'coffers/my_paid_list.html'
        context = {
            'my_coffers': my_paid_coffers
        }

        return render(request, template, context)

    elif request.method == 'POST':

        # # Check if this POST is for deleting a book
        # if (
        #     "actual_method" in form_data
        #     and form_data["actual_method"] == "DELETE"
        # ):
                
        #     contributor_coffer = ContributorCoffer.objects.get(coffer_id = coffer_id, contributor_id=request.user.contributor.id)
        #     contributor_coffer.delete()

        #     return redirect(reverse('cofferupApp:my_coffers'))    

        # else:
            form_data = request.POST

            # instantiate...
            new_contributor_coffer = ContributorCoffer(
                coffer_id = pk,
                contributor_id = request.user.id,
            )

            # and then save to the db
            print(new_contributor_coffer.admin.user.username)
            new_contributor_coffer.save()

            return redirect(reverse('cofferupApp:my_coffers'))
