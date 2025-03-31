from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)


class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    num = forms.IntegerField(label='stair')
    num = forms.IntegerField(label='year')
    num = forms.IntegerField(label='year')
    num = forms.IntegerField(label='year')
    