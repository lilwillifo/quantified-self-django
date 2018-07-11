from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViews, MealViews

urlpatterns = {
    path('foods/', FoodViews.as_view({'get': 'list', 'post': 'create'})),
    path('foods/<food_id>', FoodViews.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('meals/', MealViews.as_view({'get': 'list'})),
    path('meals/<meal_id>/foods', MealViews.as_view({'get': 'retrieve'}))
}

urlpatterns = format_suffix_patterns(urlpatterns)
