from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url


from . import views

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)