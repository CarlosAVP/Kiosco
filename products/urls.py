
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', list_products, name="list"),
    path('create/', create_product, name="create"),
    path('details/<id>', details_product, name="details"),
    path('store/', store_product, name="store"),
    path('edit/<id>', edit_product, name="edit"),
    path('update/<id>', update_product, name="update"),
    path('delete/<id>', delete_product, name="delete"),
]
