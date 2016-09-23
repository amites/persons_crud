from django.shortcuts import render

from persons.forms import PersonForm
from persons.models import Person


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }
    return render(request, 'persons/list.html', context)


