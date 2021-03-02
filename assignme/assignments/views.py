from django.shortcuts import render
from assignments.models import Assignment


def assignment_index(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignment_index.html', context)


def assignment_detail(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    context = {
        'assignment': assignment
    }
    return render(request, 'project_detail.html', context)
