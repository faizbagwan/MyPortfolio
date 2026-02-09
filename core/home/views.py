from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home_view(request):
#    return HttpResponse("Welcome to the Home Page!")

def home_view(request):
    return render(request, 'index.html')

#def about_view(request):
#    return render(request, 'AboutUs.html')

def success_page(request):
    print("*" * 10)
    return HttpResponse("Success! Your action was completed.")