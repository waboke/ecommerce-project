from django.shortcuts import render
from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    template_name ='store/home.html'
    context={'products':products}
    return render(request, template_name, context)
    