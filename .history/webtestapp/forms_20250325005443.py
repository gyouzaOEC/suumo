from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', ''),
    ('terace_town', 'オレンジ'),
    ('orange', 'オレンジ'),
)


class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')