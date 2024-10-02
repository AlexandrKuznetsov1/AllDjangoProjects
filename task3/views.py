from django.shortcuts import render
from django.views.generic import TemplateView


class myplatform(TemplateView):
    template_name = 'my_platform.html'


def shop(request):
    text1 = "Комплект снастей для рыбалки"
    text2 = "Лодка резиновая"
    text3 = "Костюм рыболова"
    context = {
        "text1": text1,
        "text2": text2,
        "text3": text3,
    }
    return render(request, 'my_shop.html', context)


def basket(request):
    return render(request, 'basket.html')