from django.urls import path

from . import views

app_name = 'address'

urlpatterns = [
    path('directions/add/', views.AddressAdd.as_view()),
    path('directions/delete/', views.AddressDelete.as_view()),
    path('directions/', views.AddressGet.as_view()),
]