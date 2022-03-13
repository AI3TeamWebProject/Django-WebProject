
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import search.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search.views.recommender, name='home'),
    path('product/', include('product.urls', namespace='product')),
    path('user/', include('users.urls', namespace='users')),
    path('order/', include('order.urls', namespace='order')),
    path('search/', include('search.urls', namespace='search')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
