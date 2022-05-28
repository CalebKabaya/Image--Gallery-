import re
from django.db import models

# Create your models here.
class Location(models.Model):
    location_name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save  

class Category(models.Model):
    category_name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save 

class Image(models.Model):
    # id = models.AutoField(primary_key=True)
    img_name=models.CharField(max_length=30)
    img_decription=models.TextField()
    img_path=models.ImageField(upload_to='pictures/')
    img_location=models.ForeignKey(Location,on_delete=models.CASCADE)
    img_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    time=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.img_name

    def save_img(self):
        self.save()

    def delete_img(self):
        self.delete 

    @classmethod
    def search_category(cls,search_term) :
        search_results = cls.objects.filter(img_category__category_name__icontains=search_term)
        return search_results

    @classmethod
    def search_location(cls,location) :
        filter_location = cls.objects.filter(img_location__location_name__icontains=location)
        return filter_location 

    @classmethod
    def get_img_by_id(cls,input_id)  :
        filt_img=cls.objects.get(id=input_id) 
        return filt_img  

    @classmethod
    def get_all(cls):
        all_images=Image.objects.all()  
        return all_images 
  
        
               

