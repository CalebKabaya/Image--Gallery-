from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class GalleryTest(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='food')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'kenya')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='apples', image_description='this is an apple',image_path='media/pictures/apples-1776744_1920.jpg',image_category=self.new_category,image_location=self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='apples')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.get(id=1).image_name,'apples')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('apples','apples')
        fetched = Image.objects.get(image_name='apples')
        self.assertEqual(fetched.get(id=1).image_name,'apples')
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)
    def test_search_by_category(self):
        self.new_image.save_image()
        fetch_specific = Category.objects.get(category_name='apples')
        self.assertTrue(fetch_specific.category_name=='food')
    def test_filter_by_location(self):
        self.new_image.save_image()
        fetch_specific = Image.filter_location('kenya')
        self.assertEqual(fetch_specific.get(id=1),self.new_image)
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Kenya')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)