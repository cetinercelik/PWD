from django import forms

from content.models import contentInput, ImagePost


class HomeForm(forms.ModelForm):
    class Meta:
        model = contentInput
        fields = "__all__"

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = "__all__"