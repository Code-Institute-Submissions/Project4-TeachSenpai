from django.contrib import admin
from django.urls import path, include
import orders.views

urlpatterns = [
    path('', orders.views.index, name="show_order_route"),
    path('create/<product_id>', orders.views.create_order, name="create_order_route"),
    path('detail/<order_id>', orders.views.view_order_details, name="view_order_detail_route")
]
