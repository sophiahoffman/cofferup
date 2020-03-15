from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile_form(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)

        template = 'profile/form.html'
        context = {
            user:user
            }

    return render(request, template, context)