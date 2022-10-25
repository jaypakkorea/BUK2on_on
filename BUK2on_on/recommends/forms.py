from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class RestaurantForm(forms.ModelForm):

    adress = forms.CharField(
        label='adress',
        widget=forms.TextInput(
            attrs={
                'class': 'adress',
                'placeholder': 'adress',
                'maxlength': 1000,
                'rows': 10,
                'cols': 50,
                }
            )
        )

    name = forms.CharField(
    label='name',
    widget=forms.TextInput(
        attrs={
            'class': 'name',
            'placeholder': 'name',
            'maxlength': 200,
            'rows': 10,
            'cols': 50,
            }
        )
    )

    stars = forms.IntegerField(
    label='stars',
    widget=forms.NumberInput(
        attrs={
            'min': 0,
            'max' : 3,
            }
        )
    )

    bestMenu = forms.CharField(
    label='bestMenu',
    widget=forms.TextInput(
        attrs={
            'class': 'bestMenu',
            'placeholder': 'bestMenu',
            'maxlength': 200,
            'rows': 10,
            'cols': 50,
            }
        )
    )

    reason = forms.CharField(
    label='reason',
    widget=forms.TextInput(
        attrs={
            'class': 'reason',
            'placeholder': 'reason',
            'maxlength': 1000,
            'rows': 10,
            'cols': 50,
            }
        )
    )

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