from django.shortcuts import render
from .forms import CommentForm
from .models import Comment, Course


def course_index(request):
    courses = Course.objects.all().order_by('-created_on')
    context = {
        "courses": courses,
    }
    return render(request, "course_index.html", context)


def course_category(request, category):
    courses = Course.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "courses": courses,
    }
    return render(request, "course_category.html", context)


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                course=course,
            )
            comment.save()

    comments = Comment.objects.filter(course=course)
    context = {
        "course": course,
        "comments": comments,
        "form": form,
    }
    return render(request, "course_detail.html", context)
