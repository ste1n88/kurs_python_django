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



## 1 WORK
def home(request):
    text = '''<h1>"Изучаем Джанго" </h1>
               <strong>Автор</strong>: <i>Капущак М.М. </i>'''
    return HttpResponse(text)

## 2 WORK
def about(request):
    about_info = f'''
                    <i>Имя:</i><strong> {f_name}</strong><br>
                    <i>Отчество:</i><strong> {l_name}</strong><br>
                    <i>Фамилия:</i><strong> {m_name}</strong><br>
                    <i>телефон:</i><strong> {phone}</strong><br>
                    <i>email:</i><strong> {email}</strong><br>
                 '''
    return HttpResponse(about_info)

## 3 4 6 WORK
def get_item(request, item_id):

    name = ''
    quantity = ''
    
    product_404 = f'''
                     <i>Товар с id {item_id}</i><strong> не найден!</strong><br>
                  '''
    go_back = '''
                 <a href="/items/">назад к списку товаров</a>
              '''

    for item in items:
        if item["id"] == item_id:
            name = item["name"]
            quantity = item["quantity"]
            product = f'''
                         <i>Название:</i><strong> {name}</strong><br>
                         <i>Количество:</i><strong> {quantity}</strong><br>
                      '''
            return HttpResponse ('%s%s' % (product, go_back) )

    return HttpResponse ('%s%s' % (product_404, go_back) )


## 5 WORK
def get_items(request, ):

    name = ''
    quantity = ''


    html = '<ol>'

    for item in items:
        name = item["name"]
        quantity = item["quantity"]
        product = f'''<li>
                     <i>Название:</i><strong> {name}</strong><br>
                     <i>Количество:</i><strong> {quantity}</strong><br></li>
                  '''
        html+=product
    html+='</ol>'

    return HttpResponse ( html)
