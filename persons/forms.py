from django.forms import ModelForm

from persons.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'zip_code', ]
