from django import forms
from onlineapp.models import *

class AddCollege(forms.ModelForm):
    class Meta:
        model=College
        exclude=['id']
        widgets={
            'name':forms.TextInput(attrs={'class':'input','placeholder':'Enter Name'}),
            'location': forms.TextInput(attrs={'class': 'input','placeholder': 'Enter Location'}),
            'acronym': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Acronym'}),
            'contact': forms.EmailInput(attrs={'class': 'input','placeholder': 'Enter Email'}),
        }

class AddStudent(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college','dropped_out']
        widgets={
            'name': forms.TextInput(
                attrs={'class': 'input','placeholder': 'Enter Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'input','placeholder': 'Enter Email'}),
            'db_folder': forms.TextInput(
                attrs={'class': 'input', 'placeholder': 'Enter DBFolder Name'}),
            'dropped_out': forms.CheckboxInput()
        }

class MockTest(forms.ModelForm):
    class Meta:
        model=MockTest1
        exclude={'id','total','student'}
        widgets={
            'problem1': forms.NumberInput(
                attrs={'class': 'input','placeholder':'Score in Problem1'}),
            'problem2': forms.NumberInput(
                attrs={'class': 'input','placeholder':'Score in Problem2'}),
            'problem3': forms.NumberInput(
                attrs={'class': 'input', 'placeholder':'Score in Problem3'}),
            'problem4': forms.NumberInput(
                attrs={'class': 'input','placeholder':'Score in Problem4'}),
        }

