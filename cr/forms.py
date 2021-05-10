from django.forms import ModelForm
from django import forms
from .models import Task
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', ]

       
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('user',
                  'cr_date', 
                  'project_name', 
                  'cr_description', 
                  'cr_project_code', 
                  'attendance_point',
                  'result_point',
                  'pm'
                  )

        labels = {
                'user': "Select Engineer",
                'cr_date': "", 
                'project_name': "", 
                'cr_description': "", 
                'cr_project_code': "", 
                'attendance_point': "出勤",
                'result_point': "作業結果",
                'pm': "PM",
        }

        widgets = {
            'user': forms.Select(attrs={'class':'form-select'}),
            'cr_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter a date, YYYY-MM-DD'}), 
            'project_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Project Name'}), 
            'cr_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter CR content'}), 
            'cr_project_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Project Code'}), 
            'attendance_point': forms.Select(attrs={'class':'form-select'}),
            'result_point': forms.Select(attrs={'class':'form-select'}),
            'pm': forms.Select(attrs={'class':'form-select'})

        }




    