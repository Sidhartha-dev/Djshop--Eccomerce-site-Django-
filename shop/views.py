from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from math import ceil

# Create your views here.


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    #params = {'no_of_slides': nSlides, 'range': range(
    #    1, nSlides), 'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]

    params= {'allProds': allProds}
    return render(request, 'shop/index.html', params)

    # return HttpResponse("Index shop")


def about(request):
    return render(request, 'shop/about.html')
    # return HttpResponse("Index shop")

# def contact(request):
    # return render(request, 'shop/contact.html')
    # return HttpResponse("Index Contact")

# def tracker(request):
#     #return render(request, 'shop/tracker.html')
#     return HttpResponse("Index Contact")

# def search(request):
#     #return render(request, 'shop/search.html')
#     return HttpResponse("Index Contact")


# def productview(request):
#     #return render(request, 'shop/search.html')
#     return HttpResponse("Index Contact")


# def checkout(request):
#     #return render(request, 'shop/checkout.html')
#     return HttpResponse("Index Contact")
