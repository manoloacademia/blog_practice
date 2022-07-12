from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post Title', max_length=50)
    text = forms.TimeField(label='Post Text')