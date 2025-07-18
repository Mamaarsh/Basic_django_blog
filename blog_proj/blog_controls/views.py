from django.shortcuts import render

def home(request):
    return render(request, "blog_controls/home.html")

def posts(request):
    pass

def post_detail(request):
    pass