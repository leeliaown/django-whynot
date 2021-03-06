from django.forms import ModelForm, widgets
from django import forms
from .models import Engineer, Task
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateEngineerForm(ModelForm):
    class Meta:
        model = Engineer
        fields = ['name', 'eng_id', 'eng_department', 'created_date', ]

        labels = {

            'eng_id': '員工ID',
            'eng_department': '員工部門'            


        }

        widgets = {

            'created_date': forms.DateInput(attrs={'type': 'date'}),

        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', ]

       
class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TaskForm, self).__init__(*args, **kwargs)
        self.initial['pm'] = self.request.user

    class Meta:
        model = Task
        fields = ('user',
                  'cr_date', 
                  'project_name', 
                  'cr_description', 
                  'cr_project_code', 
                  'attendance_point',
                  'result_point',
                  'rollback_point',
                  'pm',
                  'remark',
                  )


        labels = {
                'user': "Select Engineer",
                'cr_date': "CR date", 
                'project_name': "", 
                'cr_description': "", 
                'cr_project_code': "", 
                'attendance_point': "出勤",
                'result_point': "作業結果",
                'rollback_point': "通報點數",
                'pm': "PM (系統自動帶入)",
                'remark': "",
        }

        MONTHS = {
            1:('1月'), 2:('2月'), 3:('3月'), 4:('4月'),
            5:('5月'), 6:('6月'), 7:('7月'), 8:('8月'),
            9:('9月'), 10:('10月'), 11:('11月'), 12:('12月')
            }
        # obj = Task._meta.get_fields()
        # print(obj)
        widgets = {
            'user': forms.Select(attrs={'class':'form-select'}),
            # 'cr_date': forms.SelectDateWidget(months=MONTHS, attrs={'style': 'font-size: 15px'}),
            # 'cr_date': forms.NumberInput(attrs={'type': 'date'}),
            'cr_date': forms.DateInput(attrs={'type': 'date'}),
            'project_name': forms.HiddenInput(attrs={'class':'form-control', 'placeholder': 'Enter Project Name'}), 
            'cr_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter CR content'}), 
            'cr_project_code': forms.HiddenInput(attrs={'class':'form-control', 'placeholder': 'Enter Project Code'}), 
            'attendance_point': forms.Select(attrs={'class':'form-select'}),
            'result_point': forms.Select(attrs={'class':'form-select'}),
            'rollback_point': forms.Select(attrs={'class':'form-select'}),
            'pm': forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
            'remark': forms.TextInput(attrs={'class':'form-control', 'placeholder': '[Optional] : Enter a remark for CR ' }),

        }

        #'value': Task._meta.get_field('pm').


    