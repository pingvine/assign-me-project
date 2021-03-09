from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import HandinForm
from .models import Handin
import os


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
    absolute_path = os.getcwd() + handin.attached_files.url
    f = open(absolute_path, 'r')
    file_content = f.read()
    f.close()
    file_name = os.path.splitext(absolute_path)[0]
    file_type = handin.get_format_type()

    context = {
        "handin": handin,
        "file_content": file_content,
        "file_name": file_name,
        "file_type": file_type,
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

    return redirect('handin_detail', handin.pk)
