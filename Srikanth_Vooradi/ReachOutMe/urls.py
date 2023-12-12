# ReachOutMe/urls.py

from django.urls import path
from . import views

app_name = 'ReachOutMe'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path(r'create/', views.contact_create, name='contact_create'),
    path(r'<int:pk>/', views.contact_detail, name='contact_detail'),
    path(r'<int:pk>/update/', views.contact_update, name='contact_update'),
    path(r'<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    
]

