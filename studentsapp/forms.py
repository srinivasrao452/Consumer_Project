
from django import forms

class StudentForm(forms.Form):
    sno = forms.IntegerField()
    sname = forms.CharField()
    marks = forms.IntegerField()
    address = forms.CharField()
    mobile = forms.IntegerField()



