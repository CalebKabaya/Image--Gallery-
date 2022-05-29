from email import message
from django.shortcuts import render
from .models import Image,Category,Location
# pagination
from django.core.paginator import Paginator


# Create your views here.
def display(requests):
    all_images= Image.objects.all()
    locations=Location.objects.all()
    categories=Category.objects.all()
    # Set up Pagination
    p = Paginator(Image.objects.all(), 12)
    page = requests.GET.get('page')
    images_all = p.get_page(page)
    nums = "a" * images_all.paginator.num_pages





    title= 'Home'


    return render(requests,'index.html',{'all_images':all_images,'locations':locations,'categories':categories,'title':title,'nums':nums,'images_all':images_all})

def search_results(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Search'
    if 'searchby' in request.GET and request.GET["searchby"]:
        search_term = request.GET.get("searchby")
        searched_images=Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'single.html',{"message":message,"all_images": searched_images,'locations':locations,'categories':categories, 'title':title})

    else:
        message = "You haven't searched for any image"
        return render(request, 'index.html',{"message":message, 'locations':locations,'categories':categories, 'title':title})


def categories_display(request,category):
    categories=Category.objects.all()
    title = f"(category)"
    category_results= Image.search_category(category)
    # Set up Pagination
 

    return render(request,'index.html',{"title":title,"all_images":category_results,"categories":categories})

def location_display(request,location):
    locations=Location.objects.all()
    title = f"(location)"
    location_results= Image.search_location(location)

     # Set up Pagination
    return render(request,'index.html',{"title":title,"all_images":location_results,"locations":locations})



