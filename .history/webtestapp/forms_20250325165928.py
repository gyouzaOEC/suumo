from django import forms

TYPE_CHOICES = (
    ('house', '賃貸一戸建て'),
    ('mansion', '賃貸マンション'),
    ('terace_town', '賃貸テラス、タウンハウス'),
    ('apartment', '賃貸アパート'),
)

WARD = (
    ,中央区（Chuo-ku）
    ,千代田区（Chiyoda-ku）
    ,港区（Minato-ku）
    ,新宿区（Shinjuku-ku）
    ,文京区（Bunkyo-ku）
    ,台東区（Taito-ku）
    ,墨田区（Sumida-ku）
    ,江東区（Koto-ku）
    ,品川区（Shinagawa-ku）
    ,目黒区（Meguro-ku）
    ,大田区（Ota-ku）
    ,世田谷区（Setagaya-ku）
    ,渋谷区（Shibuya-ku）
    ,中野区（Nakano-ku）
    ,杉並区（Suginami-ku）
    ,豊島区（Toshima-ku）
    ,北区（Kita-ku）
    ,荒川区（Arakawa-ku）
    ,板橋区（Itabashi-ku）
    ,練馬区（Nerima-ku）
    ,足立区（Adachi-ku）
    ,葛飾区（Katsushika-ku）
    ,江戸川区（Edogawa-ku）
)

class dataForm(forms.Form):
    type = forms.CharField(label='種別')
    year = forms.IntegerField(label='year')
    stair = forms.IntegerField(label='stair')
    fee = forms.IntegerField(label='year')
    area = forms.FloatField(label="")
    num = forms.IntegerField(label='year')
    