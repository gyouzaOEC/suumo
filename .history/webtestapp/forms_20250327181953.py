from django import forms
from django.core.validators import MinValueValidator


TYPE_CHOICES = (
    ('賃貸一戸建て' ,'賃貸一戸建て'),
    ('賃貸マンション' ,'賃貸マンション'),
    ('賃貸テラス、タウンハウス' ,'賃貸テラス、タウンハウス'),
    ('賃貸アパート' ,'賃貸アパート'),
)

WARD_CHOICES = (
       ("中央区","中央区"),
        ("千代田区","千代田区"),
        ("港区","港区"),
        ("新宿区","新宿区"),
        ("文京区","文京区"),
        ("台東区","台東区"),
        ("墨田区","墨田区"),
        ("江東区","江東区"),
        ("品川区","品川区"),
        ("目黒区","目黒区"),
        ("大田区","大田区"),
        ("世田谷区","世田谷区"),
        ("渋谷区","渋谷区"),
        ("中野区","中野区"),
        ("杉並区","杉並区"),
        ("豊島区","豊島区"),
        ("北区","北区"),
        ("荒川区","荒川区"),
        ("板橋区","板橋区"),
        ("練馬区","練馬区"),
        ("足立区","足立区"),
        ("葛飾区","葛飾区"),
        ("江戸川区","江戸川区"),
)

SLDK_CHOICES = (
("K","K"),
("SK","SK"),
("LK","LK"),
("DK","DK"),
("SLK","SLK"),
("SDK","SDK"),
("LDK","LDK"),
("SLDK","SLDK"),
)

class DataForm(forms.Form):
    type = forms.ChoiceField(label="種別",choices=TYPE_CHOICES)
    year = forms.IntegerField(label='築年数',validators=[MinValueValidator(0)])
    stairs = forms.IntegerField(label='階',validators=[MinValueValidator(0)])
    fee = forms.IntegerField(label='管理費',validators=[MinValueValidator(0)])
    area = forms.FloatField(label="専有面積",validators=[MinValueValidator(0)])
    ward = forms.ChoiceField(label='区',choices=WARD_CHOICES)
    station = forms.CharField(label="駅")
    walk = forms.IntegerField(label='歩分',validators=[MinValueValidator(0)])
    fullbasement = forms.IntegerField(label='地下階数',validators=[MinValueValidator(0)])
    fullstairs = forms.IntegerField(label='地上階数',validators=[MinValueValidator(0)])
    rooms = forms.IntegerField(label='居室',validators=[MinValueValidator(0)])
    sldk = forms.ChoiceField(label='SLDK',choices=SLDK_CHOICES)
    