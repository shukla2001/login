from django.shortcuts import render, redirect  
from login.forms import LoginForm  
from login.models import Login 
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect()  
            except:  
                pass  
    else:  
        form = LoginForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    logins = Login.objects.all()  
    return render(request,"home.html",{'logins':logins})
def home(request):  
    logins = Login.objects.all()  
    return render(request,"show.html",{'logins':logins})    
def edit(request, id):  
    login = Login.objects.get(id=id)  
    return render(request,'home.html', {'login':login})  
def update(request, id):  
    login = Login.objects.get(id=id)  
    form = LoginForm(request.POST, instance = login)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'home.html', {'login': login})  
def destroy(request, id):  
    login = Login.objects.get(id=id)  
    login.delete()  
    return redirect("/show")  
