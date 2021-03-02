from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from assignments.models import Assignment


@login_required
def assignment_index(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignment_index.html', context)


@login_required
def assignment_detail(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    context = {
        'assignment': assignment
    }
    return render(request, 'assignment_detail.html', context)
