from django.contrib import admin
from .customer import models as customer_models

# Register your models here.
admin.site.register(customer_models.Customer)