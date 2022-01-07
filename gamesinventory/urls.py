from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_game_list, name='get_game_list'),
    path('create/', views.create_game, name='create_game'),
    path('<int:game_id>/', views.get_game_detail, name='get_game_detail'),
    path('<int:game_id>/update/', views.update_game, name='update_game'),
    path('<int:game_id>/delete/', views.delete_game, name='delete_game'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('autocomplete/full/', views.autocomplete_detail, name='autocomplete_detail'),
]