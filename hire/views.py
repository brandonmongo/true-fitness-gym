from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PT
from .forms import PTForm

# Create your views here.


def all_PTs(request):
    """ A view to display all the PTs at the gym """

    PTs = PT.objects.all().order_by("full_name")
    template = 'hire/hire_PT.html'
    hire_query = None

    if 'hire-search' in request.GET:
        hire_query = request.GET['hire-search']
        if not hire_query:
            messages.error(request, 'You didnt search anything')
            return redirect(reverse('all_PTs'))

        hire_queries = (Q(full_name__icontains=hire_query) | Q(opening_statement__icontains=hire_query))
        PTs = PTs.filter(hire_queries)
    context = {
        'PTs': PTs,
        'searched_PT': hire_query
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


@login_required
def add_PT(request):
    """ A view to add personal trainer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin has access to this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PTForm(request.POST, request.FILES)
        if form.is_valid():
            personal_trainer = form.save()
            messages.success(request, 'Successfully added a PT!')
            return redirect(reverse('PTs_details', args=[personal_trainer.slug]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        PT_form = PTForm()

    PT_form = PTForm()
    template = 'hire/add_pt.html'
    context = {
        'pt_form': PT_form
    }
    return render(request, template, context)


@login_required
def edit_PT(request, PT_slug):
    """ A view to edit personal trainer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin has access to this.')
        return redirect(reverse('home'))

    personal_trainer = get_object_or_404(PT, slug=PT_slug)
    if request.method == 'POST':
        form = PTForm(request.POST, request.FILES, instance=personal_trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('PTs_details', args=[personal_trainer.slug]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        PT_form = PTForm(instance=personal_trainer)
        messages.info(request, f'You are editing {personal_trainer.full_name} PT profile')

    template = 'hire/edit_pt.html'
    context = {
        'pt_form': PT_form,
        'personal_trainer': personal_trainer
    }
    return render(request, template, context)


@login_required
def delete_PT(request, PT_slug):
    """ A view to delete personal trainer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin has access to this.')
        return redirect(reverse('home'))

    personal_trainer = get_object_or_404(PT, slug=PT_slug)
    personal_trainer.delete()
    messages.success(request, 'PT has been removed!')
    return redirect(reverse('all_PTs'))
