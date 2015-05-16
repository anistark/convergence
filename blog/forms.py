from django import forms


class EditPosts(forms.Form):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    titleimgfile = forms.ImageField(label='Select a file')
    content = forms.CharField(min_length=20, widget=forms.Textarea(attrs={'class': 'form-control'}))

