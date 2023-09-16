from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('webapp.customer.urls')),
    path('product/', include('webapp.product.urls')),
]
