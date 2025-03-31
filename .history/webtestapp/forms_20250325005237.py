from django import forms

KIND_CHOICES = (
    ('apple', 'リンゴ'),
    ('banana', 'バナナ'),
    ('orange', 'オレンジ'),
)


class dataForm(forms.Form):
    text = forms.CharField(label='種別')
    num = forms.IntegerField(label='数量')