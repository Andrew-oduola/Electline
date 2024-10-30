from django import forms

class MatricNoLoginForm(forms.Form):
    matric_no = forms.CharField(max_length=20, label='Matriculation Number')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    