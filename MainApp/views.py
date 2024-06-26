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

######################## DAY 1

## 1 WORK
def home(request):

    context = {
        "name": "Капущак М.М.",
        "email": "ste1n88@rambler.ru",
    }

    return render(request, "index.html", context)

#    text = '''<h1>"Изучаем Джанго" </h1>
#               <strong>Автор</strong>: <i>Капущак М.М. </i>'''
#    return HttpResponse(text)

## 2 WORK
def about(request):
    context_about = {
                    'f_name': f_name,
                    'm_name': l_name,
                    'l_name': m_name,
                    'phone': phone,
                    'email': email
    }
    return render(request, "about.html", context_about)

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
            id = item["id"]
            name = item["name"]
            quantity = item["quantity"]
            context = {
                        'id': id,
                        "name": name,
                        'quantity': quantity
            }
            return render (request, "item.html", context )

    return HttpResponse ('%s%s' % (product_404, go_back) )


## 5 WORK
def get_items(request, ):

    name = ''
    quantity = ''


    html = '<ol>'

    for item in items:
        name = item["name"]
        quantity = item["quantity"]
        product = f'''<li><a href=/item/{item['id']}
                     <i>Название:</i><strong> {name}</strong><br>
                     <i>Количество:</i><strong> {quantity}</strong><br>
                     </a></li>
                  '''
        html+=product

    html+='</ol>'

    return HttpResponse ( html)

######################## DAY 2

def get_items_list(request, ):

    context = { "items" : items }

    return render(request, "items_list.html", context)
