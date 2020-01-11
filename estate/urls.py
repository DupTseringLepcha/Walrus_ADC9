from django.urls import path
from .views import *

<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 

>>>>>>> BishalGurung_Walrus_DownloadandUploadFeature
urlpatterns=[
    path('add_property',get_add_property),
=======

urlpatterns=[
    path('add_property/',get_add_property),
>>>>>>> PrajwalPandey_Walrus_SearchFeature
    path('post_add_property',post_add_property),
    path('estates_home',get_estates_home,name="estates_home"),
    path('delete_estate/<int:ID>',delete_property),
    path('update_estate/<int:ID>',get_update_property),
<<<<<<< HEAD
    path('post_update_property/<int:ID>',post_update_property)
<<<<<<< HEAD
]
=======
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('image_upload', property_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'), 
    path('property_images', display_property_images, name = 'property_images'),
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

>>>>>>> BishalGurung_Walrus_DownloadandUploadFeature
=======
    path('post_update_property/<int:ID>',post_update_property),
    path('search/',search, name= 'search' ),
    path('search/searchdata/', searchdata, name='searchdata')

]
>>>>>>> PrajwalPandey_Walrus_SearchFeature
