from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,  UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created! You are now able to login {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    context= {
        'form':form
    }
    return render(request, 'Users/register.html', context)
 
@login_required
def profile(request):
    if request.method == 'POST':
       update_form = UserUpdateForm(request.POST, instance=request.user)
       profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
       
       if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') 

    else:
            update_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    
    return render(request, 'Users/profile.html', context)





    """
    Types of messages....
    
    mesaage.debug,
    message.info,
    message.success,
    message.warning,
    message.error
    """
    









    """
    from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    """
    