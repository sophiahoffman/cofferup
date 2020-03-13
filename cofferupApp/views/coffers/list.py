import sqlite3
from cofferupApp.models import Coffer
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def my_coffers_list(request):
    if request.method == 'GET':

        all_coffers = Coffer.objects.all()

        name = request.GET.get('name', None)
        # title = request.GET['title']

        if name is not None:
            all_coffers = all_coffers.filter(user.id = request.auth.user.contributor.id)

        template = 'coffers/list.html'
        context = {
            'all_coffers': all_coffers
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # instantiate...
        coffer = Coffer(
            name = form_data['name'],
            description = form_data['description'],
            date_end = form_data['end_date'],
            admin_id = request.user.librarian.id,
        )

        # and then save to the db
        print(new_coffer.admin.user.username)
        new_coffer.save()

        return redirect(reverse('cofferupApp:coffers'))