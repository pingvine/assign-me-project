from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import HandinForm
from .models import Handin


@login_required
def handins_index(request):
    handins = Handin.objects.all().order_by('-created_on')
    context = {
        'handins': handins,
        'form': HandinForm(),
    }
    return render(request, 'handins_index.html', context)


@login_required
def handin_detail(request, pk):
    handin = Handin.objects.get(pk=pk)

    context = {
        "handin": handin,
    }
    return render(request, "handin_detail.html", context)


@login_required
def new_handin(request):
    if request.method == 'POST':
        form = HandinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = HandinForm()
    handin = form.instance

    context = {
        "form": form,
        "handin": handin,
    }
    return render(request, "handin_detail.html", context)
