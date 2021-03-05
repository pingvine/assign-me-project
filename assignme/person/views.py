from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from person.models import Person


@login_required
def person_index(request):
    persons = Person.objects.all().order_by('-first_name')
    context = {
        'persons': persons,
    }
    return render(request, 'person_index.html', context)
