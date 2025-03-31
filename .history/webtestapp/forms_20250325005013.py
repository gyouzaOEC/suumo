from django import forms

class dataForm(forms.Form):
    text = forms.CharField(label='')
    num = forms.IntegerField(label='数量')