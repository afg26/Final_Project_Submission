#importing required libraries
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views 
from user_login import views as v

#all the URLS that are attached to this app is mentioned here and all of them perform their task properly,
#has been check multiple time and no error has been seen while running them.
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name= 'login'),
    path('sign_up/' , v.sign_up, name= 'sign_up'),
    path('add-cart/<pizza_uid>/', views.add_cart , name='add_cart' ),
    path('registration/', include('django.contrib.auth.urls')),
    path('cart/', views.cart, name='cart'),
    path('remove_cart_items/<cart_items_uid>/', views.remove_cart_items, name='remove_cart_items'),
    path('orders/', views.orders, name='orders'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('about/', views.about , name= 'about'),

    path('admin/', admin.site.urls),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()