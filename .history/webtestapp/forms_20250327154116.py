from django import forms
from django.core.validators import MinValueValidator


TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)

WARD_CHOICES = (
       ("Chiyoda-ku","中央区"),
        ("Chuo-ku","千代田区"),
        ("Minato-ku","港区"),
        ("Shinjuku-ku","新宿区"),
        ("Bunkyo-ku","文京区"),
        ("Taito-ku","台東区"),
        ("Sumida-ku","墨田区"),
        ("Koto-ku","江東区"),
        ("Shinagawa-ku","品川区"),
        ("Meguro-ku","目黒区"),
        ("Ota-ku","大田区"),
        ("Setagaya-ku","世田谷区"),
        ("Shibuya-ku","渋谷区"),
        ("Nakano-ku","中野区"),
        ("Suginami-ku","杉並区"),
        ("Toshima-ku","豊島区"),
        ("Kita-ku","北区"),
        ("Arakawa-ku","荒川区"),
        ("Itabashi-ku","板橋区"),
        ("Nerima-ku","練馬区"),
        ("Adachi-ku","足立区"),
        ("Katsushika-ku","葛飾区"),
        ("Edogawa-ku","江戸川区"),
)

ward



class DataForm(forms.Form):
    type = forms.ChoiceField(choices=TYPE_CHOICES,label="種別")
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
    sldk = forms.CharField(label='SLDK')
    