from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import PT
# Create your views here.


def all_PTs(request):
    """ A view to display all the PTs at the gym """

    PTs = PT.objects.all().order_by("full_name")
    template = 'hire/hire_PT.html'
    
    if 'hire-search' in request.GET:
        hire_query = request.GET['hire-search']
        if not hire_query:
            messages.error(request, 'You didnt search anything')
            return redirect(reverse('all_PTs'))

        hire_queries = (Q(full_name__icontains=hire_query) | Q(opening_statement__icontains=hire_query))
        PTs = PTs.filter(hire_queries)
    context = {
        'PTs': PTs
    }
    return render(request, template, context)


def PTs_details(request, PT_slug):
    """ A view to display all the PTs information """
    personal_trainer = get_object_or_404(PT, slug=PT_slug)

    print(personal_trainer)
    template = 'hire/PT_detail.html'
    context = {
        'personal_trainer': personal_trainer
    }
    return render(request, template, context)
