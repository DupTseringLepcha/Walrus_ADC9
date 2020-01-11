from django.db import models

# Create your models here.

class Property(models.Model):
    property_name=models.TextField()
    price=models.IntegerField()
    property_detail=models.TextField()
<<<<<<< HEAD
    uploaded_at=models.DateTimeField(auto_now_add=True)
=======
    uploaded_at=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50) 
    property_Main_Img = models.ImageField(upload_to='images/') 
>>>>>>> BishalGurung_Walrus_DownloadandUploadFeature
