from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

f_name = 'Михаил'
l_name = 'Капущак'
m_name = 'Миронович'
phone = '8-927-687-8060'
email = 'ste1n88@rambler.ru'

items = [
            {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
            {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
            {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
            {"id": 7, "name": "Картофель фри" ,"quantity":0},
            {"id": 8, "name": "Кепка Montana" ,"quantity":124},
        ]

## 1
def home(request):
    text = '''<h1>"Изучаем Джанго" </h1>
               <strong>Автор</strong>: <i>Капущак М.М. </i>'''
    return HttpResponse(text)

## 2
def about(request):
    about_info = f'''
                    <i>Имя:</i><strong> {f_name}</strong><br>
                    <i>Отчество:</i><strong> {l_name}</strong><br>
                    <i>Фамилия:</i><strong> {m_name}</strong><br>
                    <i>телефон:</i><strong> {phone}</strong><br>
                    <i>email:</i><strong> {email}</strong><br>
                 '''
    return HttpResponse(about_info)

## 3
def get_item(request):
    item = 5
    print (request.data)
    return HttpResponseRedirect(reverse("items", args=(items,)))
