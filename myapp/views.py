from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def trail(request):
    return HttpResponse("<h1>project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")    

def profile(request):
    name="sachin"
    return render(request,"myapp/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})

def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html") 

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        second_name=request.POST.get("second_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="Female"
        else:
            gender="Male"

        send_mail("Thanks for Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(first_name,second_name),
        "sachinkn2017@gmail.com" ,[email,],fail_silently=True)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,second_name,email,password,phno,gender,date,month,year))
    return render(request,"myapp/register.html")


def multiselect(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,'multiselect.html')

from django.core.files.storage import FileSystemStorage

def img_upld(request):
    return render(request,"img_upld.html")

def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        print(image)
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)

    return render(request,"img_display.html",context={'file_url':file_url})
