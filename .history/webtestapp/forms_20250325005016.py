from django import forms

class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')