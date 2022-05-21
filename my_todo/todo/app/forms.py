
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Category,Profile,Todo

class ProfileForm(UserChangeForm):
    
    class Meta:
        model = Profile
        fields = ["img","username","first_name", "last_name","age"]
        Widget={"username":forms.TextInput(attrs={'readonly':'readonly'})}
class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["img","username","first_name", "last_name","age"]

class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","category","due_date"]

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username","password"]
   