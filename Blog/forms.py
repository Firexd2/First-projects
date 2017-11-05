from django import forms
from .models import *

class NewPost(forms.ModelForm):


    class Meta:
        model = Post
        exclude = [""]
        widgets = {
            'logo': forms.FileInput(),
        }


class NewImage(forms.ModelForm):


    class Meta:
        model = Image
        exclude = [""]