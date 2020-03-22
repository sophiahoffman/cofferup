from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def contribution_list(request, coffer_id = None):
    if request.method == 'GET':

        # all_coffers = Coffer.objects.all()
        my_contribs = ContributorCofferTransaction.objects.filter(contributor_coffer__contributor_id =request.user.id).order_by('-transaction_date')[:10]

        template = 'home.html'
        context = {
            'my_contribs': my_contribs
        }

        return render(request, template, context)

    # elif request.method == 'POST':
        # not sure where the best place to put this delete is... yet
        # # Check if this POST is for deleting a book
        # if (
        #     "actual_method" in form_data
        #     and form_data["actual_method"] == "DELETE"
        # ):
                
        #     coffer = Coffer.objects.get(coffer_id = coffer_id)
        #     coffer.delete()

        #     return redirect(reverse('cofferupApp:coffers'))  

        # else:

    if request.method == "POST":

        form_data = request.POST

        # instantiate...
        new_coffer_contribution = ContributorCofferTransaction(
            contributor_coffer_id = coffer_id,
            description = form_data['description'],
            amount = form_data['amount'],
        )

        # and then save to the db
        new_coffer_contribution.save()

        return redirect(reverse('cofferupApp:my_coffers'))
