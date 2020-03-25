from django.shortcuts import render
from django.contrib.auth.models import User
from cofferupApp.models import Contributor
from django.contrib.auth.decorators import login_required


@login_required
def profile_form(request):
    if request.method == "GET":
        contributor = Contributor.objects.get(id=request.user.id)

        template = 'profile/form.html'
        context = {
            contributor:contributor
            }

    return render(request, template, context)