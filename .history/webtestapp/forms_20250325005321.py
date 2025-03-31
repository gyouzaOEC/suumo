from django import forms

TYPE_CHOICES = (
    ('house', 'リンゴ'),
    ('banana', 'バナナ'),
    ('orange', 'オレンジ'),
)


class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')