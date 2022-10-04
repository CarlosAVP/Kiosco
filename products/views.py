from django.shortcuts import redirect, render, get_object_or_404
from .models import Product


def list_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create_product(request):
    return render(request, 'create.html')


def details_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'details.html', {'product': product})


def store_product(request):
    new_product = Product(
        name=request.POST['name'],
        stock=request.POST['stock'],
        barcode=request.POST['barcode'],
        price=request.POST['price'],
    )
    new_product.save()
    return redirect('products:list')


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'edit.html', {'product': product})


def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = request.POST['name']
    product.barcode = request.POST['barcode']
    product.price = request.POST['price']

    product.save()

    return redirect('products:list')


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    product.delete()
    return redirect('products:list')
