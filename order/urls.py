from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order/create/', views.OrderCreate.as_view()),
    path('order/', views.OrderGet.as_view()),
]
