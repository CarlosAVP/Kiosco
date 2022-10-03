from django.shortcuts import redirect, render
from .models import Product

# Create your views here.

def list_products(request): 
  products = Product.objects.all()
  return render(request, 'index.html', { 'products': products })
  