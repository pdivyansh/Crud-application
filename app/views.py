from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def insert(request):
    return render(request,'insert.html')

def InsertData(request):
    # data come from html to views
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    email=request.POST['email']
    contact=request.POST['contact']
    # creating objects of model class 
    # inserting data into tables
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    return redirect('show')

def show(request):
    # select * from tables
    # for fetching all the data of the tables
    all_data=Student.objects.all()
    return render(request,'show.html',{'key1':all_data})

# editpage view
def edit(request,pk):
    # fetching the data of particular id
    get_data=Student.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})
# updata view
def UpdateData(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Firstname=request.POST['firstname']
    udata.Lastname=request.POST['firstname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']

    # query for update
    udata.save()
    return redirect('show')

# delete data view
def DeleteData(request,pk):
    ddata=Student.objects.get(id=pk)
    # query for delete
    ddata.delete()
    return redirect('show')
