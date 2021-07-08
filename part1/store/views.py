from django.shortcuts import render

# Create your views here.
from store.models import Product, Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context=context)
