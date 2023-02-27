
from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    
]
