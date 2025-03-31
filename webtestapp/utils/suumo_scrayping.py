import requests
from bs4 import BeautifulSoup
from retry import retry
import urllib
import time
import pandas as pd
from sklearn import datasets
data_samples = []

# スクレイピングするページ数
max_page = 300
# SUUMOを東京都23区のみ指定して検索して出力した画面のurl(ページ数フォーマットが必要)
url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&page={}'

# リクエストがうまく行かないパターンを回避するためのやり直し
@retry(tries=3, delay=10, backoff=2)
def load_page(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup

# -15行目まで-
for page in range(1,max_page+1):
    before = time.time()
    # ページ情報
    soup = load_page(url.format(page))
    # 物件情報リストを指定
    mother = soup.find_all(class_='cassetteitem')

    # 物件ごとの処理
    for child in mother:

        # 建物情報
        data_home = []
        # カテゴリ
        data_home.append(child.find(class_='ui-pct ui-pct--util1').text)
        # 建物名
        data_home.append(child.find(class_='cassetteitem_content-title').text)
        # 住所
        data_home.append(child.find(class_='cassetteitem_detail-col1').text)
        # 最寄り駅のアクセス
        children = child.find(class_='cassetteitem_detail-col2')
        for id,grandchild in enumerate(children.find_all(class_='cassetteitem_detail-text')):
            data_home.append(grandchild.text)
        # 築年数と階数
        children = child.find(class_='cassetteitem_detail-col3')
        for grandchild in children.find_all('div'):
            data_home.append(grandchild.text)

        # 部屋情報
        rooms = child.find(class_='cassetteitem_other')
        for room in rooms.find_all(class_='js-cassette_link'):
            data_room = []

            # 部屋情報が入っている表を探索
            for id_, grandchild in enumerate(room.find_all('td')):
                # 階
                if id_ == 2:
                    data_room.append(grandchild.text.strip())
                # 家賃と管理費
                elif id_ == 3:
                    data_room.append(grandchild.find(class_='cassetteitem_other-emphasis ui-text--bold').text)
                    data_room.append(grandchild.find(class_='cassetteitem_price cassetteitem_price--administration').text)
                # 敷金と礼金
                elif id_ == 4:
                    data_room.append(grandchild.find(class_='cassetteitem_price cassetteitem_price--deposit').text)
                    data_room.append(grandchild.find(class_='cassetteitem_price cassetteitem_price--gratuity').text)
                # 間取りと面積
                elif id_ == 5:
                    data_room.append(grandchild.find(class_='cassetteitem_madori').text)
                    data_room.append(grandchild.find(class_='cassetteitem_menseki').text)
                # url
                elif id_ == 8:
                    get_url = grandchild.find(class_='js-cassette_link_href cassetteitem_other-linktext').get('href')
                    abs_url = urllib.parse.urljoin(url,get_url)
                    data_room.append(abs_url)
            # 物件情報と部屋情報をくっつける
            data_sample = data_home + data_room
            data_samples.append(data_sample)

    # 1アクセスごとに1秒休む
    time.sleep(1)
df =pd.DataFrame(data_samples,columns=["種別","物件名","住所","最寄り＿1","最寄り＿2","最寄り＿3",\
    "築年数","全階数","階","賃料","管理費","敷金","礼金","間取り","専有面積","url"])

df = df.iloc[:,:15]

df.to_csv('output1.csv')