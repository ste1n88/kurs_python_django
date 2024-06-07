from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


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
            form.save()
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
        snip = Snippet.objects.get(pk=snip_id)
    except ObjectDoesNotExist:
        return HttpResponse(f'Item with id={snip_id} not found')
    else:
        context = {
                  'pagename': 'Просмотр сниппетов',
                  'snip': snip,
        }
        print (context)
        return render (request, "pages/snippet.html", context)

#def snippet_create(request, ):
#    if request.method == 'POST':
#        name = request.POST['field_name']
#        lang = request.POST['field_lang']
#        code = request.POST['field_code']
#        snippet = Snippet(name=name, lang=lang, code=code)
#        snippet.save()
#        return redirect('sniplist')

