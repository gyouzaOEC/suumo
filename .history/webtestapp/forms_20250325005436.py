from django import forms

TYPE_CHOICES = (
    ('house', 'い'),
    ('mansion', ''),
    ('terace_town', 'オレンジ'),
    ('orange', 'オレンジ'),
)


class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')