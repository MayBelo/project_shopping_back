
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product/<pk>/',views.single_product),
    path('cart/',views.items),
    path('cartUpdate/<pk>',views.single_item),
    path('cartAdd/', views.items),
    path('cart/<pk>/',views.single_cart_item),
    path('cartDelete/<pk>/',views.single_item),
    path('search/', views.search),
    path('rings/', views.ring)


    

    # path('update_cart/<pk>/',views.update_cart),
  



    
]
