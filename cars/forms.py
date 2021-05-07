from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        exclude = ['by', 'uploaded', 'slugy']

class UploadPic(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('mainpic', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5')