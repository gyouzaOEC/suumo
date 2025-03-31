from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)

WARD = 

class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    stair = forms.IntegerField(label='stair')
    fee = forms.IntegerField(label='year')
    area = forms.FloatField(label="")
    num = forms.IntegerField(label='year')
    