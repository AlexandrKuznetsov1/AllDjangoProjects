from django.shortcuts import render


def pattern_class(request):
    return render(request, 'class_template.html')


def pattern_func(request):
    return render(request, 'func_template.html')