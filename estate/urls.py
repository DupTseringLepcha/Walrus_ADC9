from django.urls import path
from .views import *

from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns=[
    path('add_property',get_add_property),
    path('post_add_property',post_add_property),
    path('estates_home',get_estates_home,name="estates_home"),
    path('delete_estate/<int:ID>',delete_property),
    path('update_estate/<int:ID>',get_update_property),
    path('post_update_property/<int:ID>',post_update_property)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('image_upload', hotel_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'), 
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)

