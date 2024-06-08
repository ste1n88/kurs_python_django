from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth

def login(request):
   if request.method == 'POST':
       username = request.POST.get("field_user")
       password = request.POST.get("field_pass")
       print("username =", username)
       print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           context = {
                      'pagename': 'PythonBin',
                      'errors': ['Wrong username or password', ],
           }
           return render(request, 'pages/index.html', context)
   return redirect('home')
   #return redirect(request.META.get('HTTP_REFERER', '/'))

def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


#def add_snippet_page(request):
#    context = {'pagename': 'Добавление нового сниппета'}
#    return render(request, 'pages/add_snippet.html', context)

def add_snippet_page(request):
    if request.method == 'GET':    # Получить пустую форму для заполнения
        form = SnippetForm()
        context = {
                   'pagename': 'Просмотр сниппетов',
                   'form': form,
        }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == 'POST':    # Если хотим создать новую запись
        form = SnippetForm(request.POST)
        if form.is_valid():
            snip = form.save(commit=False)    # чтобы не было двойных коммитов: Сохрани, но не записывай в БД
            if request.user.is_authenticated:
                snip.user = request.user    # Сохранение сниппета с полем User
                snip.save() 
            return redirect('sniplist')
        return render(request, 'pages/add_snippet.html', {'form': form} )


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
               'pagename': 'Просмотр сниппетов',
               'snippets': snippets,
               'count': len(snippets),
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, snip_id):
    try:
        snip = Snippet.objects.get(id=snip_id)
    except ObjectDoesNotExist:
        return HttpResponse(f'Item with id={snip_id} not found')
    else:
        context = {
                  'pagename': 'Просмотр сниппетов',
                  'snip': snip,
                  'type': 'view',
        }
        print (context)
        return render (request, "pages/snippet.html", context)

def delete_snippet(request, snip_id):
#    print("snip_id: ", snip_id)
    snip = Snippet.objects.get(id=snip_id)
    snip.delete()
    return HttpResponseRedirect( request.META.get('HTTP_REFERER'))

def update_snippet(request, snip_id):
    try:
        snip = Snippet.objects.get(id=snip_id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == 'GET':
        context = {
                  'pagename': 'Редактирование сниппета',
                  'snip': snip,
                  'type': 'update',
        }
        print (context)
        return render (request, "pages/snippet.html", context)
    if request.method == 'POST':
        form_data = request.POST
        snip.name = form_data['field_name']
        snip.code = form_data['field_code']
        snip.creation_date = form_data['creation_date']
        snip.save()
        return redirect('sniplist')


#def snippet_create(request, ):
#    if request.method == 'POST':
#        name = request.POST['field_name']
#        lang = request.POST['field_lang']
#        code = request.POST['field_code']
#        snippet = Snippet(name=name, lang=lang, code=code)
#        snippet.save()
#        return redirect('sniplist')

