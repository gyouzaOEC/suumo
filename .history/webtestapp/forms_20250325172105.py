from django import forms

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

class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    stair = forms.IntegerField(label='stair')
    fee = forms.IntegerField(label='year')
    area = forms.FloatField(label="")
    ward = forms.IntegerField(label='year')
    walk = forms.IntegerField(label='year')
    fullbasement = forms.IntegerField(label='year')
    fullstair = forms.IntegerField(label='year')
    rooms = forms.IntegerField(label='year')
     = forms.IntegerField(label='year')
    