from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Order, Customer
from .forms import OrderForm, CustomerForm, CreateUserForm
from .filters import OrderFilter

# Create your views here.

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = { 'form': form }
        return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')

        context = {  }
        return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    orders_out_delivery = orders.filter(status='Out of delivery').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        'orders_out_delivery': orders_out_delivery
    }
    return render(request, 'accounts/dashboard.html', context)

login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(
        request,
        'accounts/products.html',
        {'products': products}
    )

login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = { 
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
        'my_filter': my_filter
    }

    return render(request, 'accounts/customer.html', context)

login_required(login_url='login')
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order,
        fields=('product', 'status'),
        extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})

    # if post redirect, otherwise order_form page
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer) 
        if formset.is_valid():
            formset.save()
            return redirect('/') 
    context = { 'formset': formset }
    return render(request, 'accounts/order_form.html', context)

login_required(login_url='login')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = { 'form': form }
    return render(request, 'accounts/order_form.html', context)

login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/') 
    context = { 'item': order }
    return render(request, 'accounts/delete.html', context)

login_required(login_url='login')
def create_customer(request):
    form = CustomerForm()
    # if post redirect, otherwise order_form page
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = { 'form': form }
    return render(request, 'accounts/customer_form.html', context)
