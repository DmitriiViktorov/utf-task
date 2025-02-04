from django.urls import path
from .views import FoodListView, FoodListTemplateView


urlpatterns = [
    path('api/v1/foods/', FoodListView.as_view(), name='food-list'),
    path('foods/', FoodListTemplateView.as_view(), name='food-list-template'),
]
