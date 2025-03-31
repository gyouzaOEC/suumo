from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)

WARD = (
       ("Chiyoda-ku",(中央)区),
        ("Chuo-ku",(千代田)区),
        ("Minato-ku",(港)区),
        ("Shinjuku-ku",(新宿)区),
        ("Bunkyo-ku",(文京)区),
        ("Taito-ku",(台東)区),
        ("Sumida-ku",(墨田)区),
        ("Koto-ku",(江東)区),
        ("Shinagawa-ku",(品川)区),
        ("Meguro-ku",(目黒)区),
        ("Ota-ku",(大田)区),
        ("Setagaya-ku",(世田谷)区),
        ("Shibuya-ku",(渋谷)区),
        ("Nakano-ku",(中野)区),
        ("Suginami-ku",(杉並)区),
        ("Toshima-ku",(豊島)区),
        ("Kita-ku",(北)区),
        ("Arakawa-ku",(荒川)区),
        ("Itabashi-ku",(板橋)区),
        ("Nerima-ku",(練馬)区),
        ("Adachi-ku",(足立)区),
        ("Katsushika-ku",(葛飾)区),
        ("Edogawa-ku",(江戸川)区),
)

class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    stair = forms.IntegerField(label='stair')
    fee = forms.IntegerField(label='year')
    area = forms.FloatField(label="")
    num = forms.IntegerField(label='year')
    