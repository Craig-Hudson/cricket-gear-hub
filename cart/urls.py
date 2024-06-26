from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<item_key>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<item_key>/',
         views.remove_from_cart, name='remove_from_cart'),
]
