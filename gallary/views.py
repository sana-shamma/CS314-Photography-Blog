from django.shortcuts import render
# Create your views here.

def baby(request):
    return render(request,'gallary/baby.html')

def country(request):
    return render(request,'gallary/country.html')

def product(request):
    return render(request,'gallary/product.html')
