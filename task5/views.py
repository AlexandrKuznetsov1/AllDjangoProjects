from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

users = ['Alex', 'Anna', 'Jack']
info = {}


# Использование класса Django:
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #  обработка данных формы:
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data["age"]
            subscribe = form.cleaned_data["subscribe"]

            print(f"'Name' {name}")
            print(f"'password' {password}")
            print(f"'repeat_password' {repeat_password}")
            print(f"'age' {age}")
            print(f"'subscribe' {subscribe}")

            if password == repeat_password and age >= 18 and name not in users:
                users.append(name)
                return HttpResponse(f"Приветствуем, {name}!")
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse(f"Ошибка, {info['error']}!")
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse(f"Ошибка, {info['error']}!")
            if name in users:
                info['error'] = f'Пользователь {name} уже существует'
                return HttpResponse(f"Ошибка, {info['error']}!")

    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


# Использование шаблона html:
def sign_up_by_html(request):
    if request.method == "POST":
        # получаем данные со стороны пользователя:
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        subscribe = request.POST.get('subscribe') == 'on'

        print(f"'Name' {name}")
        print(f"'password' {password}")
        print(f"'repeat_password' {repeat_password}")
        print(f"'age' {age}")
        print(f"'subscribe' {subscribe}")
        # http ответ пользователю
        if password == repeat_password and age >= 18 and name not in users:
            users.append(name)
            return HttpResponse(f"Приветствуем, {name}!")
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if name in users:
            info['error'] = f'Пользователь {name} уже существует'
            return HttpResponse(f"Ошибка, {info['error']}!")
    # если это Get-запрос:
    return render(request, 'registration_page.html', context=info)


