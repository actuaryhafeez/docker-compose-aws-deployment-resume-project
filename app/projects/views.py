from django.shortcuts import render

# Create your views here.
def projects(request):
    context = {'projects': 'active'}
    return render(request, 'projects.html', context)
