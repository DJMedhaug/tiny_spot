from django import forms

from .models import SignUp, Post
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please varify your email address")
    message = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                label="Leave empty",
                                validators=[must_be_empty]
                                )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError("Please enter the same email")


class SignUpForm(forms.ModelForm):  # clean methods used to clean data in email and full_name.
    honeypot = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                label="Leave empty",
                                validators=[must_be_empty]
                                )

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name


class PhotoUploadForm(forms.Form):
    # Keep name to 'file' because that's what Dropzone is using
    file = forms.ImageField(required=True)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

