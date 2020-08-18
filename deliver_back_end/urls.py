from django.contrib import admin
from django.urls import path, include

from dataBaseTestPop.factory import ProductFactory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),

]

for _ in range(2):
    ProductFactory.create()
