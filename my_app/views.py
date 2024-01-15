from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request=request,template_name="index.html")

def login(request):
    return render(request=request,template_name="login.html")