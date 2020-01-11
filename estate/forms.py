from django import forms 
from .models import *
  
class PropertyForm(forms.ModelForm): 
  
    class Meta: 
        model = Property 
        fields = ['name', 'property_Main_Img'] 
