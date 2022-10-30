from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from .custom_widgets import PreviewImageFileWidget


class RestaurantForm(forms.ModelForm):

    adress = forms.CharField(
        label='Adress',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'adress',
                'maxlength': 1000,
                'size': 40,
                }
            ),
        )

    name = forms.CharField(
    label='Name',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'name',
            'maxlength': 200,
            'size': 40,
            }
        )
    )

    stars = forms.IntegerField(
    label='Stars',
    widget=forms.NumberInput(
        attrs={
            'placeholder': '-',
            'min': 0,
            'max' : 3,
            }
        )
    )

    bestMenu = forms.CharField(
    label='Best Menu',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'Best Menu',
            'maxlength': 200,
            'size': 40,
            }
        )
    )

    reason = forms.CharField(
    label='Comment',
    widget=forms.Textarea(
        attrs={
            'placeholder': 'Reason',
            'maxlength': 1000,
            'rows' :4,
            'cols' :42,
            }
        )
    )

    class Meta:
        model = Restaurant
        exclude = ['user']

 
 
class ImageForm(forms.ModelForm):

    image = forms.ImageField(
    required = True,
    label='Image',
    widget=forms.FileInput(),
    error_messages={
        'required': '사진을 입력하세요.',
    })

    
    class Meta:
        model = Images
        fields = ('image', )
        labels = {
            'image': _('Image'),
        }
        