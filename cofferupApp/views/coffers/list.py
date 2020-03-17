import sqlite3
from cofferupApp.models import Coffer, ContributorCoffer
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def coffers_list(request):
    if request.method == 'GET':

        added_coffers = ContributorCoffer.objects.filter(contributor_id =request.user.id) 
        unique_unadded_coffers = []
        for coffer in added_coffers:
            unique_unadded_coffers.append(coffer.coffer.id)

        all_coffers = Coffer.objects.exclude(id__in=unique_unadded_coffers)

        template = 'coffers/list.html'
        context = {
            'all_coffers': all_coffers
        }

        return render(request, template, context)

    elif request.method == 'POST':
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
        form_data = request.POST

        # instantiate...
        new_coffer = Coffer(
            name = form_data['name'],
            description = form_data['description'],
            date_start = form_data['date_start'],
            date_end = form_data['date_end'],
            admin_id = request.user.id,
        )

        # and then save to the db
        new_coffer.save()

        return redirect(reverse('cofferupApp:coffers'))