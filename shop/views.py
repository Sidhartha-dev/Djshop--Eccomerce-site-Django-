from django.shortcuts import render
from .models import Product
from .models import Contact
from .models import Orders
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
    #return HttpResponse("Index shop")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(name, email, phone, message)
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    
    return render(request, 'shop/contact.html')
    # return HttpResponse("Index Contact")

def tracker(request):
    return render(request, 'shop/tracker.html')
#     return HttpResponse("Index Contact")

# def search(request):
#     #return render(request, 'shop/search.html')
#     return HttpResponse("Index Contact")


def productView(request, myid):
    #fetch product using id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})
#     return HttpResponse("Index Contact")


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        #print(name, email, phone, message)
        order = Orders(name=name, email=email, phone=phone, address=address, address2=address2, city=city, state=state, zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
    return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
#     return HttpResponse("Index Contact")
