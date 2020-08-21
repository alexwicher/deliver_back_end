from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from product import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('categories/', views.CategoriesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)