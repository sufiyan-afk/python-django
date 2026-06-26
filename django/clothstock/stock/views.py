from django.shortcuts import render,redirect
from stock.models import Stock
# Create your views here.

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request ,'stock_list.html',{'stocks':stocks})

def add_stock(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        material = request.POST.get('material')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        Stock.objects.create(name = name ,
                             category = category ,
                             material = material ,
                             quantity = quantity ,
                             price = price)
        return redirect('stock_list')
    else:
        return render(request,'add_stock.html')