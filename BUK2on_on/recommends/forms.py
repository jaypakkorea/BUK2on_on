from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

 
 
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )
        labels = {
            'image': _('Image'),
        }