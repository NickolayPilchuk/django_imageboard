from django import forms
from .models import Threads,Comments


class Thread_form(forms.ModelForm):
    class Meta:
        model = Threads
        fields = ['text','image']

class Comment_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text','image']