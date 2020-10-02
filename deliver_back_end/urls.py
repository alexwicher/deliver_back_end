from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from dataBaseTestPop.factory import ProductFactory
from deliver_back_end import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('user.urls')),
    path('', include('address.urls')),
    url(r'^auth/', include('djoser.urls')),
]

# comment this for when executing migrate and makemigrations
# uncomment this for when executing runserver to populate DB

# ----------------
for _ in range(2):
    ProductFactory.create()
# ----------------
