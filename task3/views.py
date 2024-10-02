from django.shortcuts import render
from django.views.generic import TemplateView


class myplatform(TemplateView):
    template_name = 'my_platform.html'


def shop(request):
    return render(request, 'my_shop.html')


def basket(request):
    return render(request, 'basket.html')