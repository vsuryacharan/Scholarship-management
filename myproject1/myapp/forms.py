# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser,loggers
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']




class logger_forms(forms.ModelForm):
    class Meta:
        model = loggers
        fields = ['user','is_selected']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user=user
        self.fields['is_selected'].widget = forms.CheckboxInput(attrs={'class': 'checkbox'})
    

    def save(self, commit=True):
        instance = super().save(commit=False)
         

        if commit:
            instance.save()

        return instance
 
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
