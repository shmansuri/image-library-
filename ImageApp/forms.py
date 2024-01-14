from django import forms 
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # it includes all field of model
        fields = '__all__'
        label=[{'photo':"select Image"}]
        