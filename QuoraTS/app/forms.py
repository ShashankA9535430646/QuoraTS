from django import forms
from .models import Question,Answer
from django.contrib.auth.models import User

class form1(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('query','content')

class form2(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('query_answer','content','likes')

class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

