from django.shortcuts import render
from django.views.generic import TemplateView




class pattern_class(TemplateView):
    template_name = 'class_template.html'


def pattern_func(request):
    return render(request, 'func_template.html')