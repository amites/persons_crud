from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from persons.forms import PersonForm
from persons.models import Person


def update_persons(request, person_id=None):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('person_id'):
                messages.success(request, 'Person updated.')
            else:
                messages.success(request, 'Person added.')
            return HttpResponseRedirect(reverse('persons:list'))
    elif person_id:
        try:
            obj = Person.objects.get(pk=person_id)
            form = PersonForm(instance=obj)
        except Person.DoesNotExist:
            messages.error(request, 'Person does not exist.')
            form = PersonForm()
    else:
        form = PersonForm()

    context = {
        'form': form,
        'person_id': person_id,
    }
    return render(request, 'persons/create.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }
    return render(request, 'persons/list.html', context)


def delete_persons(request, person_id):
    try:
        obj = Person.objects.get(pk=person_id)
        obj.delete()
        messages.success(
            request, 'Person {first_name} {last_name} deleted.'.format(
                **obj.__dict__))
    except Person.DoesNotExist:
        messages.error(request, 'Person does not exist.')
    return HttpResponseRedirect(reverse('persons:list'))
