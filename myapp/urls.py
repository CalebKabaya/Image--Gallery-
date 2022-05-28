from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url


from . import views

urlpatterns=[
    re_path('^$',views.display,name = 'display'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^category/(\w+)', views.categories_display,name='categories_display'),
    re_path(r'^location/(\w+)', views.location_display,name='location_display'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)