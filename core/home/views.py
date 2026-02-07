from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home_view(request):
#    return HttpResponse("Welcome to the Home Page!")

def home_view(request):

    peoples = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28},
        {"name": "Eve", "age": 22},
    ]

 #   for people in peoples:
  #      print(people)
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium, facilis vel? Laborum, a nemo nihil dolorem quia corporis facere hic, aspernatur quod, necessitatibus laudantium eligendi vitae aliquam repudiandae quo assumenda!"""


    return render(request, 'index.html',context={ "peoples": peoples, "text": text})




def success_page(request):
    print("*" * 10)
    return HttpResponse("Success! Your action was completed.")