from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.inbox, name='chats'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:recipe_pk>/', views.new_chat, name='new'),
]