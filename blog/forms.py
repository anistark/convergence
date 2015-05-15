from django import forms

from .models import Post,User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post # post is from model


class UserForm(forms.ModelForm):
	class Meta:
		model = User # post is from model