from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'name':'Aditi'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = val1 + val2
    return render(request, 'result.html', {'result' : val3})

def dashboard(request):
    return render(request,'dashboard.html')

def pricing(request):
    return render(request,'pricing.html')

def features(request):
    return render(request,'features.html')

def settings(request):
    return render(request,'settings.html')