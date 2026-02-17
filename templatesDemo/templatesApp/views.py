from django.shortcuts import render

# Create your views here.
def my_Template(request):
    myDict = {"name":"Antika"}
    return render(request,'templatesApp/firstTemplate.html',context=myDict)

def employee(request):
    myDict={'id':56344,"name":"Antika","sal":10000}
    return render(request,'templatesApp/employeeTemplate.html',myDict)
