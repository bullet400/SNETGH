from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customer, Product, Order
from accounts.forms import OrderForm, CustomerForm, CreatUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from .models import Customer

# Create your views here.

@login_required(login_url='login')
def home(request):
    orders =Order.objects.all()
    customers =Customer.objects.all()
    total_customer =customers.count()
    total_order =orders.count()

    delivered =orders.filter(status ='Delivered').count()

    pend_order =orders.filter(status ='Pending').count()
    out_delivery =orders.filter(status ='Out for Delivery').count() 

    context ={'orders': orders, 'customers':customers,'total_customer':total_customer,
    'total_order':total_order, 'delivered':delivered, 'pend_order':pend_order, 'out_delivery':out_delivery}
    return render(request,'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products =Product.objects.all()
    total_products =products.count()
    context ={'products':products, 'total_products':total_products}
    return render(request, 'accounts/products.html', context)

@login_required(login_url='login')
def customers(request,cust_id):    
    customer =Customer.objects.get(id =cust_id)
    cust_orders = customer.order_set.all().order_by('-date_created')
    total_orders =cust_orders.count()
    context ={'customer':customer,'cust_orders':cust_orders, 'total_orders':total_orders}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url ='login')
def creat_customer(request):
    form =CustomerForm()
    if request.method =='POST':
        form =CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer saved successfully')
            return redirect('home')
    context ={'form':form}
    customers =Customer.objects.all()
    return render(request, 'accounts/create_customers.html', context)

@login_required(login_url ='login')
def update_customer(request, cust_id):
    customer = Customer.objects.get(id= cust_id)
    form =CustomerForm(instance=customer)
    if request.method =='POST':
        form =CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        messages.success(request,("Customer updated successfully"))
        return redirect('home')
    context ={'form':form}
    return render(request,'accounts/create_customers.html', context)

@login_required(login_url='login')
def delete_customer(request, cust_id):
    customer =Customer.objects.get(id =cust_id)
    customer.delete()
    messages.success(request,("Customer deleted "))
    return redirect('home')
    #messages.success(request,("Customer deleted "))

@login_required(login_url='login')
def create_order(request, pk):
    #product = Product.objects.get(id =pk)
    #form =OrderForm( initial={'customer':customer, 'product':product})
    #OrderFormset =inlineformset_factory(parent model-> Customer, Child ->Order, fields from the child -> fields=()
    # num_of_fields -> extra =4)
    OrderFormset = inlineformset_factory(Customer, Order, fields =('product','status'), extra =2)
    customer =Customer.objects.get(id = pk)
    formset =OrderFormset(queryset =Order.objects.none(), instance = customer)
    if request.method =='POST':
        formset =OrderFormset(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            messages.success (request, 'Order(s) successfully created')
            return redirect ('/')
    context ={'formset':formset}
    return render (request, 'accounts/create_order.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    order =Order.objects.get(id =pk)
    form =OrderForm(instance=order)
    if request.method =='POST':
        form =OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, ("Order updated"))
            return redirect('home')
    context ={'form':form}
    return render (request, 'accounts/update_order.html', context)

def delete_order(request, order_id):
    orders =Order.objects.get(id =order_id)
    orders.delete()
    return redirect('home')

@login_required(login_url='login')
def del_order(request, order_id):
    dele_ord =Order.objects.get(id =order_id)
    if request.method =='POST':
        dele_ord.delete()
        return redirect('/')
    context ={'del_ord':dele_ord}
    return render(request, 'accounts/delete_order.html', context)

def payment(request):
    return render(request, 'accounts/payment.html')

def register(request):
    #redirect to home page if user is login
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form =CreatUserForm()
        if request.method =='POST':
            form =CreatUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                first_name =form.cleaned_data.get('first_name')
                last_name =form.cleaned_data.get('last_name')
                user =first_name +" "+ last_name
                group = Group.objects.get(name ='customer')
                user.group.add(group)
                Customer.objects.create(user =user)
                messages.success(request, (f"User account created successfully for {user[:10]}.... You can login now!"))
                return redirect ('login')
    context ={'form':form}
    return render (request, 'accounts/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect ('/')
    else:
        if request.method !='POST':
            return render (request, 'accounts/login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            login_user =authenticate(request, username =username, password=password)
            if login_user is not None:
                login(request, login_user)
                messages.success(request, "You've login as "+ login_user.email)
                return redirect('home')
            else:
                messages.warning(request, 'Email or password is incorrect')
                return render(request,'accounts/login.html')
            
def logoutUser(request):
    logout(request)
    return redirect ('login')

def customerPage(request):
    # orders =request.user.customer.order_set.all()

    # context ={"orders":orders}
    context ={}
    return render (request, 'accounts/user.html', context)
    