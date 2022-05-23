import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .models import Post
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_text', 'content_text', 'category',  'image')
        widgets = {
            'header_text':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_text', 'content_text', 'image')
        widgets = {
            'header_text':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


