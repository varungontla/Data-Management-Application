from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class UploadForm(forms.Form):
    title = forms.CharField()
    pdf = forms.FileField()


class SharedForm(forms.Form):
    UserName = forms.CharField(max_length=120)
    SharedFileName = forms.CharField(max_length=120)
    SharedFile = forms.FileField()


class EmailForm(forms.Form):
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=120)
    attachment = forms.Field(widget=forms.FileInput)
    message = forms.CharField(widget=forms.Textarea)
