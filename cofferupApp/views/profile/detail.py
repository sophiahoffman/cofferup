from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def user_detail(request):
    if request.method == 'GET':

        profile = User.objects.get(pk=request.user.id)


        template = 'profile/detail.html'
        context = {
            'profile': profile
        }

        return render(request, template, context)


    elif request.method == 'POST':
        form_data = request.POST
        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PATCH"
        ):
                    
            user = User.objects.get(pk=request.user.id)
            user.first_name = form_data["first_name"]
            user.last_name = form_data["last_name"]
            user.save()
        
        return redirect(reverse('cofferupApp:profile'))