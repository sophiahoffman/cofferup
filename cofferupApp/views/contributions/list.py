from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def contribution_list(request, coffer_id = None):
    # if request.method == 'GET':

    #     # all_coffers = Coffer.objects.all()
    #     all_unadded_coffers = ContributorCoffer.objects.filter(contributor_id =request.user.id) 
    #     unique_unadded_coffers = []
    #     for coffer in all_unadded_coffers:
    #         unique_unadded_coffers.append(coffer.coffer.id)
    #         print("im adding", coffer.coffer.id)

    #     all_coffers = Coffer.objects.exclude(id__in=unique_unadded_coffers)

    #     template = 'coffers/list.html'
    #     context = {
    #         'all_coffers': all_coffers
    #     }

    #     return render(request, template, context)

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