from django import forms
from .models import *

class NewPost(forms.ModelForm):

    class Meta:
        model = Post
        exclude = [""]
        widgets = {
            'logo': forms.FileInput(),
            'name_url': forms.TextInput(attrs={'id': 'url_name', 'class': 'input'}),
            'tittle': forms.TextInput(attrs={'id': 'tittle', 'class': 'input'})
        }


class NewImage(forms.ModelForm):


    class Meta:
        model = Image
        exclude = [""]