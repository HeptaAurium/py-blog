from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blogs(request):
    return render(request, 'blogs.html')

def createBlog(request):
    return render(request, 'createBlog.html')