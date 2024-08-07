"""
URL configuration for tourism_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tourism_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete/<str:item_type>/<int:item_id>/', views.confirm_delete, name='confirm_delete'),
    
    # Tours
    path('tours/', views.tour_list, name='tour_list'),
    path('tours/add/', views.add_tour, name='add_tour'),
    
    # Services
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.add_service, name='add_service'),
    
    # Clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    
    # Operators
    path('operators/', views.operator_list, name='operator_list'),
    path('operators/add/', views.add_operator, name='add_operator'),
    
    # Orders
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),
]
