import pandas as pd
from sklearn import datasets
from summo_data import datas as data


df = pd.DataFrame(data,colums=["種別","物件名","住所","最寄り＿1","最寄り＿2","最寄り＿3",\
    "築年数","全階数","","","","",])
df

print()