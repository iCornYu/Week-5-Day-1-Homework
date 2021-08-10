from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    favorite_food = [
        'Popcorn Chicken',
        'Ramen',
        'Pizza',
        'French fries',
        'KBBQ'
    ]
    context = {'foods': favorite_food}
    return render(request, 'blog/index.html', context)


