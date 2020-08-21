from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


from dataBaseTestPop.factory import ProductFactory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),

]

for _ in range(2):
    ProductFactory.create()
