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
        
               

