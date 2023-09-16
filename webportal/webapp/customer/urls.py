from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='customer_list'),
    path('customer/list', views.list, name='customer_list'),
    path('customer/add', views.add, name='add_customer'),
    path('customer/edit/<int:id>', views.edit, name='edit_customer'),
    path('customer/delete/<int:id>', views.delete, name='delete_customer'),
]