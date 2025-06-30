from django import forms
from .models import Tweet

class tweetform(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['text','photo']
