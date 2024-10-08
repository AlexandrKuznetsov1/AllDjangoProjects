from django.shortcuts import render
from django.views.generic import TemplateView


class myplatform(TemplateView):
    template_name = 'my_platform.html'


def shop(request):
    context = {
        "products": [
            "Комплект снастей для рыбалки", "Лодка резиновая", "Костюм рыболова"
        ],
    }
    return render(request, 'my_shop.html', context)


def basket(request):
    return render(request, 'basket.html')
