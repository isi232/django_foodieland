from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def recipes(request):
    return render(request, 'pages/recipes.html')

def blog(request):
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')
