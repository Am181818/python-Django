from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request,"employee _register\employee_list.html")

def employee_form(request):
    if request.method=="GET":
        form=EmployeeForm()
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        form=  EmployeeForm(request.POST)
        if form.is valid():
            form.save()
        return redirect('/employee/list')        
    return

def employee_delete(request):
    return    
















