from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def display(requests):
    all_images= Image.objects.all()
    locations=Location.objects.all()
    categories=Category.objects.all()
    title= 'Home'


    return render(requests,'index.html',{'all_images':all_images,'locations':locations,'categories':categories,'title':title})

