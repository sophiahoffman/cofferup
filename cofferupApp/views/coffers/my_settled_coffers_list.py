from cofferupApp.models import Coffer, ContributorCoffer, ContributorCofferTransaction
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def my_settled_coffers_list(request, coffer_id = None):
    if request.method == 'GET':

        """ settled coffers are coffers that are paid by an individual.
        filters contributor coffer join so only those with contributor id matching the logged in user are returned; then uses that filter on contributor coffer transaction to get only those that are paid"""

        my_paid_coffers = ContributorCoffer.objects.filter(contributor_id=request.user.id, is_settled=True)

        template = 'coffers/my_paid_list.html'
        context = {
            'my_coffers': my_paid_coffers
        }

        return render(request, template, context)

    elif request.method == 'POST':
        
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PATCH"
        ):        


            contributor_coffer = ContributorCoffer.objects.get(pk=coffer_id)
            contributor_coffer.is_settled = True
            contributor_coffer.save()

            return redirect(reverse('cofferupApp:my_settled_coffers'))
