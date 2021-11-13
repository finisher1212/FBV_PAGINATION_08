from django.shortcuts import render,redirect
from .models import Laptop
from .forms import Laptopform
from django.core.paginator import Paginator
# Create your views here.

def HomeView(request):
    template_name = 'firstapp/Home.html'
    return render(request,template_name)

def Addlaptopview(request):
    form=Laptopform()
    if request.method == 'POST':
        form=Laptopform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')
    template_name='firstapp/AddOrder.html'
    context={'form':form}
    return render(request,template_name,context)

def Showlaptopview(request):
    ord=Laptop.objects.all()
    template_name='firstapp/Showorder.html'
    context={'ord':ord}
    return render(request,template_name,context)

def Updatelaptopview(request,update):
    lap=Laptop.objects.get(id=update)
    form=Laptopform(instance=lap)
    if request.method == 'POST':
        form=Laptopform(request.POST,instance=lap)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='firstapp/Addorder.html'
    context={'form':form}
    return render(request,template_name,context)

def Deletelaptopview(request,delete):
    lap=Laptop.objects.get(id=delete)
    lap.delete()
    return redirect('show')

def listing(request):
    laptop_list = Laptop.objects.all()
    paginator = Paginator(laptop_list, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    
    context = {'page_obj': page_obj}
    template_name='firstapp/Showorder.html'

    return render(request,template_name,context )