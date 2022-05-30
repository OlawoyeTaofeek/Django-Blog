import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
       
        
        
"""ModelForm allows us to create a form that will work with a specific database model"""      
class UserUpdateForm(forms.ModelForm):  
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
"""Create A PROFILE UPDATE FORM FOR UPDATING OUR IMAGE"""
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio', 'location']

