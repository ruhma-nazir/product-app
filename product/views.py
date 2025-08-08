import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from product.models import Product

# Create your views here.


def createproduct(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = float(request.POST["price"])
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price must be positive")
        except ValueError as e:
            return render(
                request,
                "createproduct.html",
                {
                    "error": str(e),
                    "name": name,
                },
            )
        obj = Product(name=name, description=description, price=price)
        obj.save()
        return HttpResponse("<h1>Product has been created Succesfully")
    elif request.method == "GET":
        return render(request, "createproduct.html")


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


def updateproduct(request):
    if request.method == "POST":
        productid = request.POST.get("productid")
        product = Product.objects.get(id=productid)
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        price = float(request.POST["price"])
        if price < 0:
            return render(
                request,
                "createproduct.html",
                {"error": "price must be a positive number"},
            )
        product.price = price
        product.in_stock = request.POST.get("in_stock")
        product.save()
        return HttpResponse("<h1>Product has been updated successfully.</h1>")
    elif request.method == "GET":
        product = Product.objects.all()
        products_data = list(
            product.values("id", "name", "description", "price", "in_stock")
        )
        return render(
            request,
            "updateproduct.html",
            {"products": product, "json_products": json.dumps(products_data)},
        )


def home(request):
    return render(request, "home.html")


def products(request):
    if request.method == "GET":
        product = Product.objects.all()
        return render(request, "products.html", {"products": product})
