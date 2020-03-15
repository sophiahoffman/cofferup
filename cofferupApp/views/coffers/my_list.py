import sqlite3
from cofferupApp.models import Coffer, ContributorCoffer
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def my_coffers_list(request):
    if request.method == 'GET':

        all_my_coffers = ContributorCoffer.objects.filter(contributor_id = request.user.contributor.id)
        all_my_coffers_list = []
        for coffer in all_my_coffers:
            all_my_coffers_list.append(coffer.coffer.id)

        my_coffers = Coffer.objects.filter(id__in=all_my_coffers_list)
        


        template = 'my_coffers/list.html'
        context = {
            'my_coffers': my_coffers
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
            print(request)

            # instantiate...
            new_contributor_coffer = ContributorCoffer(
                coffer_id = request.pk,
                contributor_id = request.user.contributor.id,
            )

            # and then save to the db
            print(new_contributor_coffer.admin.user.username)
            new_contributor_coffer.save()

            return redirect(reverse('cofferupApp:my_coffers'))