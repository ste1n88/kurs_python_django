from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


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
                  'id': snip.id,
                  "name": snip.name,
                  'lang': snip.lang,
        }
        return render (request, "item.html", context)


