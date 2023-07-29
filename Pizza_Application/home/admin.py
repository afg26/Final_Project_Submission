#Importing required libraries
from django.contrib import admin
from .models import *

# Register your models here.
# We do have to modify our models in django framework inside the the built in django admin page too
# Which is done for this app
admin.site.register(PizzaCategory)
admin.site.register(Pizza)
admin.site.register(Cart)
admin.site.register(cart_item)
