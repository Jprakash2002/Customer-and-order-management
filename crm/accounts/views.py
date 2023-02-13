from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.forms import inlineformset_factory

def dashboard(request):
    orders=Order.objects.all()
    customerss=Customer.objects.all()
    totord=orders.count();
    totdel=orders.filter(status="delivered").count()
    pending=orders.filter(status="pending")
    context={'orders':orders,'customers':customerss,'totord':totord,'totdel':totdel,'pending':pending}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    products=Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})
def customers(request,cusid):
    customer=Customer.objects.get(id=cusid)
    orders=customer.order_set.all()
    
    totord=orders.count()
    context={'customer':customer,'orders':orders,'totord':totord}
    return render(request,'accounts/customer.html',context)

def createorder(request,cusid):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=cusid)
    
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        #form=Order(request.POST)
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/createorder.html',context)

def updateorder(request,ordid):
    order=Order.objects.get(id=ordid)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/updateorder.html',context)

def deleteorder(request,ordid):
    order=Order.objects.get(id=ordid)
    context={'order':order}
    if request.method=='POST':
        order.delete()
        return redirect('/')
    return render(request,'accounts/deleteorder.html',context)



