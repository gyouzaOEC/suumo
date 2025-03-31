from django import forms

TYPE_CHOICES = (
    ('house', 'リンゴ'),
    ('mansion', 'バナナ'),
    ('orange', 'オレンジ'),
    ('orange', 'オレンジ'),
)


class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')