from django.urls import path

from . import views

app_name = 'recipe'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit_recipe/', views.edit_recipe, name='edit_recipe'),
    path(route='<int:pk>/delete/', view=views.delete_recipe, name='delete_recipe'),
    path('new_recipe/', view=views.new_recipe, name='new_recipe'),
    path(route='browse/', view=views.browse, name='browse')
]
