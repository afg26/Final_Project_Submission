#importing required library
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import Sum





#making this class to easily import our data from section to section
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True





#creating our first and main class;
class PizzaCategory(BaseModel):
    category_name=models.CharField(max_length=200)


#creating the main Pizza class that will have the specifations of the mentioned above
class Pizza(BaseModel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name='pizzas')
    pizza_name= models.CharField(max_length=200)
    price = models.FloatField(default=100)
    images= models.ImageField(upload_to='pizza')





#creating the cart setup and class:
class Cart(BaseModel):
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='cart')
    is_paid= models.BooleanField(default=False)

    def get_total(self):
        return cart_item.objects.filter(cart= self).aggregate(Sum('pizza__price'))['pizza__price__sum']
   
    

#creating the Cart set up so that when we are adding from the different types of pizza it can display that.
class cart_item(BaseModel):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)

   