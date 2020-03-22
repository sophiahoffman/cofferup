from django.shortcuts import render

def about(request):
    if request.method == 'GET':
        template = 'about.html'
        context = {}

        return render(request, template, context)