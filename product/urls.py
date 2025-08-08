from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("products/create", views.createproduct, name="createproduct"),
    path("products/delete", views.deleteproduct, name="deleteproduct"),
    path("products/<int:id>/", views.displayproduct, name="displayproduct"),
    path("products/update", views.updateproduct, name="updateproduct"),
]
