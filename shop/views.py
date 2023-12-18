from django.shortcuts import render
from datetime import datetime
from .models import Product, Purchase


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def purchase(request):
    post = request.POST
    total_cost = 0
    purchase_dict = {}
    context = {'purchase': []}
    for p in post:
        if post[p] and 'quantity' in p:           
                purchase_dict['product_id'] = p.split(' ')[1]
                if int(post[p]) > 0:
                    purchase_dict['quantity_purchased'] = post[p]
                    purchase_dict['address'] = post['address']
                    purchase_dict['person'] = post['person']
                    person = post['person']
                    product = Product.objects.get(id=p.split(' ')[1])
                    purchase_dict['price'] = product.price
                    total_cost += product.price    
                    Purchase.objects.create(**purchase_dict)
                    context['purchase'].append(purchase_dict | dict(name=product.name))
    context['total_cost'] = total_cost
    context['person'] = person
    return render(request, 'shop/purchase.html', context)
