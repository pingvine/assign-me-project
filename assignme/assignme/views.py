from django.shortcuts import render


def error_404(request, exception, template_name='404.html'):
    context = {}
    return render(request, '404.html', context)


def error_500(request, template_name='500.html'):
    context = {}
    return render(request, '500.html', context)
