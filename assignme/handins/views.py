from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def handins_index(request):
    context = {}
    return render(request, 'handins_index.html', context)
