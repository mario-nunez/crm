from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Order, Customer

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending
    }
    return render(
        request,
        'accounts/dashboard.html',
        context
    )

def products(request):
    products = Product.objects.all()
    return render(
        request,
        'accounts/products.html',
        {'products': products}
    )


def customer(request):
    return render(request, 'accounts/customer.html')
