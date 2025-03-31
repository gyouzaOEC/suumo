import pandas as pd
from sklearn import datasets
from summo_data import datas as data


df = pd.DataFrame(data,columns=["種別","物件名","住所","最寄り＿1","最寄り＿2","最寄り＿3",\
    "築年数","全階数","階","賃料","管理費","敷金","礼金","間取り","専有面積","url"])
df = df.loc()

print(df)