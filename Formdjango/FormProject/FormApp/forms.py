from django import forms
from django.forms import ModelForm
from .models import Applicant




class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicantForm(ModelForm):
    class Meta:
        model=Applicant
        fields=('name','address','zip_code','phone','DateOfBirth', 'web', 'gender','email_address','paid')

        # labels={

        #     'name':"",
        #     'address':"",
        #     'zip_code':"",
        #     'phone':"",
        #     'web':"",
        #      'gender':"",
        #      'email_address':"",
        #      'paid':'Click this if you have paid'
             

        # }

        widgets={
            # 'name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Full Name (Surname first)'}),
            # 'address' :forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Valid Address'}),
            # 'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip code'}),
            # 'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'DateOfBirth':DateInput(),
            # 'web': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'web address'}),
            'gender': forms.RadioSelect(),
            # 'email_address': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'abc@mail.com'}),
            'paid': forms.CheckboxInput()
        }


