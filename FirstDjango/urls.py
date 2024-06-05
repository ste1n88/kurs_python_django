from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('item/<int:item_id>/', views.get_item, name='item'),
    path('items/', views.get_items),
    path('items_list/', views.get_items_list, name='items-list'),
]
