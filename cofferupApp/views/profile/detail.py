from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def user_detail(request):
    if request.method == 'GET':

        profile = User.objects.get(pk=request.user.contributor.id)


        template = 'profile/detail.html'
        context = {
            'profile': profile
        }

        return render(request, template, context)