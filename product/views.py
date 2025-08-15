import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from product.models import Product
from .forms import *
# Create your views here.


def createproduct(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            price = float(form.cleaned_data["price"])
            in_stock = form.cleaned_data["in_stock"]
            obj = Product(
                name=name, description=description, price=price, in_stock=in_stock
            )
            obj.save()
            return HttpResponse("<h1>Product has been created Succesfully")
    elif request.method == "GET":
        form = ContactForm()
        return render(request, "createproduct.html", {"form": form})


def deleteproduct(request):
    if request.method == "POST":
        productid = request.POST.get("productid")
        product = Product.objects.get(id=productid)
        product.delete()
        return HttpResponse("<h1>Product has been deleted")
    elif request.method == "GET":
        productsdata = Product.objects.all()
        return render(request, "deleteproduct.html", {"products": productsdata})


def displayproduct(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        return render(request, "displayproduct.html", {"product": product})



def updateproduct(request,p_id):
    # product = Product.objects.get(id=p_id)
    product = get_object_or_404(Product, {id: p_id})
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data["name"]
            product.description = form.cleaned_data["description"]
            product.price = float(form.cleaned_data["price"])
            product.in_stock = form.cleaned_data["in_stock"]
            product.save()
            return HttpResponse("<h1>Product has been updated successfully.</h1>")
    
    elif request.method == "GET":
        form = ContactForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'in_stock': product.in_stock,
        })
        return render(
            request,
            "updateproduct.html",
            {
                "product": product,
                "form": form,
            },
        )
    
def home(request):
    return render(request, "home.html")


def products(request):
    if request.method == "GET":
        product = Product.objects.all()
        return render(request, "products.html", {"products": product})
