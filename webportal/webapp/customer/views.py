from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Customer
from django.db.models import Q

# Create your views here.

def list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        customers = Customer.objects.filter(Q(name__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q))
    else:
        customers = Customer.objects.all()
    p = Paginator(customers,5)
    page = request.GET.get('page')
    customers = p.get_page(page)
    context = {
        'customers': customers,
    }
    return render(request, 'customer/list.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'customer/add.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new_customer = Customer(name=name, email=email, phone=phone)
        new_customer.save()
        return redirect('customer_list')

def edit(request, id):
    if request.method == 'GET':
        customer = Customer.objects.get(id=id)
        context = {'customer': customer}
        return render(request, 'customer/edit.html', context)
    else:
        customer = Customer.objects.get(id=id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.save()
        return redirect('customer_list')

def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('customer_list')