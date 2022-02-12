from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    # don't know why but this looks very noob type of code
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)

    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age' )

