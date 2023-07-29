#Importing required libraries
from django.apps import AppConfig



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'



    # A simple function that show the counter on your Cart button on top of the page,
    # how it works "it is going to count whenever you add somoething in your cart and displays that."
    def ready(self):
        from django.contrib.auth.models import User
        def get_cart_count(self):
            from models import cart_item
            return cart_item.objects.filter(cart__is_paid = False, cart__user = self).count()
            
        
        User.add_to_class("get_cart_count", get_cart_count)
