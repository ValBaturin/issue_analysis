from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name your analysis somehow'
        }
    ))
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your analysis goes here'
        }
    ))

    class Meta:
        model = Post
        fields = ('title', 'post')
