from django.urls import path 
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls), 
    path('pers', views.pers, name='pers'),
    path('show_person', views.show_person, name='show_person'),
    path('edit_person/<int:id>', views.edit_person, name='edit_person'),
    path('update_person/<int:id>', views.update_person, name='update_person'),
    path('delete_person/<int:id>', views.delete_person, name='delete_person'),
    path('get_client_info', views.get_client_info, name='get_client_info'),
]
