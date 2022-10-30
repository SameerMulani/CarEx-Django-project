from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Brands,Cars,Review
from .forms import Search , SearchHist,DispReview
from django.contrib import messages      #for popup messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Brands, Cars

# Create your views here.

def home(request):
    try:          
        data1 = Cars.objects.all()    
        data2 = Brands.objects.all()
        data3 = Review.objects.all()
        form = DispReview
        if request.method == 'POST':
            myData = DispReview(request.POST)
            if myData.is_valid():
                myData.save()
                messages.success(request,'Review added')
                return redirect('home')
        searchForm = SearchHist()
        context = {
        'Brands':data2,'Cars':data1, 'searchForm':searchForm,'review':data3}
    except Exception as e:
         context = {'Brands':'Data Not Found'}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def search(request):
    fetchBrand = request.GET['brand_name']
    fetchCar = request.GET['car_name']
    data = Cars.objects.filter(name=fetchCar)
    context = {'Cars':data}
    return render(request,'search.html',context)

@login_required(login_url='login')
def comparison(request):
    fetchBrand1 = request.GET['brand1']
    fetchBrand2 = request.GET['brand2']
    fetchCar1 = request.GET['car1']
    fetchCar2 = request.GET['car2']
    data1 = Cars.objects.filter(name=fetchCar1)
    data2 = Cars.objects.filter(name=fetchCar2)
    context = {'Car1':data1,'Car2':data2}
    return render(request,'comparison.html',context)

@login_required(login_url='login')
def brands(request):
    data = Brands.objects.all()
    context = {'brands':data}
    
    return render(request,'brands.html',context)

def loginpage(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request,username=name,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in')
            return redirect('home')
        else:
            messages.warning(request,'Invalid credentials!!')
            return redirect('login')

    return render(request,'login.html')

def logoutpage(request):
    messages.success(request,'Logged out')
    logout(request)
    return render(request,'index.html')

def car_detail(request,id):
    data = Cars.objects.filter(brand=id)
    context = {'cars':data}
    return render(request,'car_detail.html',context)

@login_required(login_url='login')
def compare(request):
    try: 
        data1 = Brands.objects.all()         
        data2 = Cars.objects.all()    
        context = {'Cars':data2,'Brands':data1}
    except Exception as e:
         context = {'Cars':'Data Not Found'}
    return render(request,'compare.html',context)

#SIGNUP:
def signup(request):
    return render(request,'accounts/signup.html')



# def ajax_car(request):
#     b = request.GET['brandName']
#     carss = Cars.objects.filter(brand=b)
#     context = {'carss':carss}
#     return render(request,'ajaxcar.html',context)
