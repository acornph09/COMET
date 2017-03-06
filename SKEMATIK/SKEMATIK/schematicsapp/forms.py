from django import forms


class UploadImageForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
