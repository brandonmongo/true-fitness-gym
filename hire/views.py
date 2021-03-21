from django.shortcuts import render
from .models import PT
# Create your views here.


def all_PTs(request):
    """ A view to display all the PTs at the gym """

    PTs = PT.objects.all()
    template = 'hire/hire_PT.html'
    context = {
        'PTs': PTs
    }

    return render(request, template, context)
