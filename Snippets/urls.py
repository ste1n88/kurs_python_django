from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snipadd'),
    path('snippets/list', views.snippets_page, name='sniplist'),
    path('snippets/<int:snip_id>', views.snippet_detail, name='snip-det'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
