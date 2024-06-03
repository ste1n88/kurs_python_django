from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about', views.about),
    path('item/<int:item>/', views.get_item, name='items'),
]
