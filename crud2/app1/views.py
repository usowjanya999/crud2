from django.shortcuts import render,redirect
from app1.models import Employee
from django.contrib import messages



def showIndex(request):
    return render(request,'index.html')

def add_employee(request):
    return render(request,"add_employee.html")

def save_emp(request):
    no = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    #query to save record into db
    Employee(idno=no, name=na, salary=sal).save()
    return redirect("add_employee")

def view_all(request):
    #query to read all records from db
    res = Employee.objects.all()
    return render(request,"view_all.html",{"data":res})

def show_update(request):
    no = request.GET.get("t1")
    result = Employee.objects.get(idno=no)
    return render(request,"update.html",{"data":result})

def update_emp(request):
    no = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    #query to update a record
    Employee.objects.filter(idno=no).update(name=na,salary=sal)
    return redirect('view_all')

def delete_emp(request):
    no = request.GET.get("no")
    #query to delete 1 record
    Employee.objects.filter(idno=no).delete()
    return redirect('view_all')
