from django.shortcuts import render
from .models import Product
from .models import Contact
from .models import Orders
from .models import OrderUpdate
import json
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
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(name, email, phone, message)
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank':thank})
    # return HttpResponse("Index Contact")

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order= Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
            
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
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        #print(name, email, phone, message)
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, address2=address2, city=city, state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order placed successsfully")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank,'id':id})
    return render(request, 'shop/checkout.html')
#     return HttpResponse("Index Contact")
