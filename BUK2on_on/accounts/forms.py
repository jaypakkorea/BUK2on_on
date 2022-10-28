from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(
        required = False,
        label='email',
        widget=forms.TextInput(
            attrs={
                'class': 'email',
                'placeholder': 'Required',
                'maxlength': 255,
            }
        )
    )





    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email','date_of_birth','instagram_url','twitter_url','facebook_url','youtube_url','profile_pic')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name','date_of_birth')
