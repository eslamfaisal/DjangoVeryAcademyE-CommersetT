from django.shortcuts import get_object_or_404, render

# Create your views here.
from store.models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context=context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product}
    return render(request, 'store/products/details.html', context=context)


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filfaketer(category=category)
    context = {'category': category, 'products': product}
    return render(request, 'store/products/category.html', context=context)
