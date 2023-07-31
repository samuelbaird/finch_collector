from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('finches/<int:finch_id>/unassoc_food/<int:food_id>/', views.unassoc_food, name='unassoc_food'),
    path('food/create/', views.FoodCreate.as_view(), name='food_create'),
    path('food/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
    path('food/', views.food_index, name='food_index'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
]