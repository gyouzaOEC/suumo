from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)

WARD = (
    ,中央区
    ,千代田区
    ,港区
    ,新宿区
    ,文京区
    ,台東区
    ,墨田区
    ,江東区
    ,品川区
    ,目黒区
    ,大田区
    ,世田谷区
    ,渋谷区
    ,中野区
    ,杉並区
    ,豊島区
    ,北区
    ,荒川区
    ,板橋区
    ,練馬区
    ,足立区
    ,葛飾区
    ,江戸川区（Edogawa-ku）
)

class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    stair = forms.IntegerField(label='stair')
    fee = forms.IntegerField(label='year')
    area = forms.FloatField(label="")
    num = forms.IntegerField(label='year')
    