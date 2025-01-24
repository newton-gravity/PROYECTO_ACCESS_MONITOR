from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import (Provincia,Municipio, Client,ClientAddress, Suscription, SuscriptionType, Game, GameCategory)




# Create your views here.

def register(request):    
    
    if request.method == 'POST':
        data = request.POST.copy()
        
        user = User.objects.create_user(username = data['registerUsername'],
                                        email=data["registerEmail"],
                                        password=data["registerPassword"])
        print("created User:", user)
        user.is_staff=False
        user.save()
        return HttpResponseRedirect("login")

    return render(request, "register.html")



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
    
        if user is not None and user.is_active:
            auth.login(request,user)
            print("User log in:",user)
            return HttpResponseRedirect("/",)
        else:
            return HttpResponse("<h2>Login Error, Please try again</h2><a href='login'>login</a>")
    
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")


def search(request):
    message=""
    results = ""
    if request.method =="GET":
        search_query = request.GET["search_text"]
        if search_query:
            qset = (
                Q (game_name__contains = search_query)|
                Q(developer__contains = search_query)                
            )
            results = Game.objects.filter(qset).distinct()
            
            if results:
                message = "Resultados para: " + search_query
            else:
                message = " NADA QUE MOSTRAR"
        else:
            results = ""
            
    return render(request,"home.html", {"games": results, "messages":message})


def home(request):
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login")
    
    else:         
        results = Game.objects.all()
        return render(request,"home.html", {"games": results})      
    
