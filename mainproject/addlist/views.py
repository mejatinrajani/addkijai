from django.shortcuts import render,redirect
from .models import Products

def home(request):
    
    return render(request,'home.html')

def businessmanpanellogin(request):
    return render(request,"businessman_panellogin.html")

def businessmanpanel(request):
    my_objects = Products.objects.all()
    context = {
        'my_objects':my_objects
    }
    return render(request,"businessmanpanel.html",context)

def addproduct(request):
    if(request.method == 'POST'):
        product_name = request.POST.get("title1")
        product_price = request.POST.get("price1")
        product_description = request.POST.get("description1")
        product_image = request.FILES['image1']
        new_product = Products(productname=product_name,productprice=product_price,productdescription=product_description,productimage=product_image)
        new_product.save()
        return redirect("businessmanpanel")
    
    return render(request,"addproduct.html")

def deleteproduct(request):
    return render(request,"deleteproduct.html")