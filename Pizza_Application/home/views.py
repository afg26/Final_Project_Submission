#importing required libraries
from site import USER_SITE
from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


#all the views that are written here and mentioned here and all of them perform their task properly,
#has been check multiple time and no error has been seen while running them.

# Create your views here.
#our first view that is our homepage
def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, 'home.html', context)



#when you are logged in you can add items from home page to add cart page 
@login_required(login_url='/registration/login/')
def add_cart(request , pizza_uid):
    user = request.user
    pizza_obj = Pizza.objects.get(uid = pizza_uid)
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)

    cart_items = cart_item.objects.create(
        cart = cart,
        pizza = pizza_obj

    )
    return redirect('/')

#once you add the items here you can go and see what you have added and the total price and price for each of the item added.
@login_required(login_url='/registration/login/')
def cart(request):
    cart = Cart.objects.get(is_paid = False, user= request.user)
    context = {'carts': cart}
    return render(request, 'cart.html', context)


#if you want to remove anything you have added in the cart, this is the function that is doing the task.
@login_required(login_url='/registration/login/')
def remove_cart_items(request, cart_items_uid):
    cart_item.objects.get(uid=cart_items_uid).delete()
    return redirect('/cart')


#this is page can give you the summary of your orders and by clicking the print receipt button "which is not donig anything at the moment" you can print your receipt.
#this is the last step of the app too.
@login_required(login_url='/registration/login/')
def orders(request):
    cart = Cart.objects.get(is_paid = False, user= request.user)
    context = {'carts': cart}
    return render(request, 'order.html', context)



#this is when you logout of the app
@login_required(login_url='/registration/login/')
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")



#a simpple about page
def about(request):
    return render(request, 'about.html')



#By going to to templates you can have a look at the html pages that is related to all these fucntions and performing their task accordingly.
#unforunately I tried my best to make a good looking sign up and login page but due to my system configuration I wasn't able to succeed and as of now this is the same
#django built in design, I did try to make my own configuration but it was looking ever more uglier, the other reason is also lack of time.

