from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def welcomepage(request):
    return HttpResponse("Welcome to Django Application!")

def homepage(request):
    html = """
    <body>
    <h1>Hello, Django</h1>
    <p>This is darshan, stuying BCA with data analytics 3rd year and i'm living in siruseri town</p>
    </body>
    """
    return HttpResponse(html)

def mainPage(request):
    return redirect("conPage")

def contentPage(request):
    return HttpResponse("<h2>This is contentpage</h2>")

def homepage(request):
    name = "Darshan"
    return render(request,"Firstapp/homepage.html",{"name":name})

def aboutPage(request,name,age):
    person = {
        "name":"darshan",
        "age":20,
        "city":"Chennai",
        "gender":"Male",
        "hobby":"Playing badminton",
        "profession":"Student"
    }
    return render(request, "Firstapp/aboutPage.html", person)

def indexPage(request,name,age):
    return redirect("aboutInfo",name=name,age=age)