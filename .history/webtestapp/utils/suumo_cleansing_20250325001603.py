import pandas as pd
import re
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np



def data_cleansing(csv):

  df = pd.read_csv(csv,encoding='shift_jis')
  df_y = df.loc[:,"賃料"]
  df_y = df_y.str.replace("万円","")
  df_y = df_y.astype(np.float64)

  df_x = df.drop(["Unnamed: 0","賃料","敷金","礼金","最寄り＿2","最寄り＿3","物件名"],axis=1)


  # df_x['間取り'].unique()

  # 種別
  dummies = pd.get_dummies(df_x['種別'],drop_first=True)
  df_x = pd.concat([df_x, dummies], axis=1)


  # 住所
  def ward_azana_separate(address):
      """区で分離する関数"""
      match = re.search(r'東京都(.+?)区([^0-9]+)', address)
      return match.group(1), match.group(2)



  df_x[['区', '字']] = df_x['住所'].apply(lambda x: pd.Series(ward_azana_separate(x)))
  df_x['区'] = df_x['区']+"区"
  df_x['字'] = df_x['字'].str.replace(r'\d+', '', regex=True)


  # 最寄り

  def station_walk_separate(nearest):
      """区で分離する関数"""
      match = re.search(r'/(.+?) 歩([0-9]+)分', nearest)
      if match:
        return match.group(1), int(match.group(2))
      else:
        match = re.search(r'/(.+?) 車([0-9]+)分', nearest)
        # 徒歩→自動車（都市部） 約4倍らしい
        return match.group(1), int(match.group(2))*4




  df_x[['最寄り駅', '歩分']] = df_x['最寄り＿1'].apply(lambda x: pd.Series(station_walk_separate(x)))

  # 築年数

  df_x['築年数'] = df_x['築年数'].str.replace("築","")
  df_x['築年数'] = df_x['築年数'].str.replace("年","")
  df_x['築年数'] = df_x['築年数'].fillna(0)
  df_x.loc[df_x["築年数"] == "新" ,'築年数'] = 0
  df_x['築年数'] = df_x['築年数'].astype(np.int16)


  # 全階数の変換
  def base_stair_separate(stair):
      """階数を分離する関数"""
      match = re.search(r'地下(\d+)地上(\d+)階建', stair)
      if match:
          return int(match.group(1)), int(match.group(2))
      else:
          match = re.search(r'(\d+)階建', stair)
          if match:
            return 0, int(match.group(1))
          else:
            # 平屋
            return 0, 1


  df_x[['地下階数', '地上階数']] = df_x['全階数'].apply(lambda x: pd.Series(base_stair_separate(x)))



  # 階

  def higher_getter(second_stair):
      """-で分離する関数"""
      match = re.search(r'([0-9]+)-([0-9]+)', second_stair)
      if match:
          return int(match.group(2))
      else:
          try:
              if "-B" in second_stair:
                match = re.search(r'([0-9]+)-B([0-9]+)', second_stair)
                return -int(match.group(2))
              if "B" in second_stair:
                second_stair = "-"+second_stair
              return int(second_stair)
          except ValueError:
              return 1

  df_x['階'] = df_x['階'].str.replace("階","")
  df_x["階"] = df_x["階"].apply(lambda x: pd.Series(higher_getter(x)))
  df_x['階'] = df_x['階'].astype(np.int32)


  #管理費
  df_x['管理費'] = df_x['管理費'].str.replace("円","")
  df_x['管理費'] = df_x['管理費'].str.replace("-","0")
  df_x['管理費'] = df_x['管理費'].astype(np.int32)

  #間取り
  def room_separate(rooms):
      """居室とLDKを分離する関数"""
      match = re.search(r'([0-9]+)([A-Z]+)', rooms)
      return int(match.group(1)), match.group(2)

  df_x["間取り"] = df_x["間取り"].str.replace("ワンルーム","1R")
  df_x[['居室', 'SLDK']] = df_x['間取り'].apply(lambda x: pd.Series(room_separate(x)))
  SLDK = ['S','L','D','K']
  for x in SLDK:
      df_x[x] = 0
      condition = df_x['間取り'].map(lambda y: bool(re.search(x,y)))
      df_x.loc[condition,x] = 1



  # 専有面積
  df_x['専有面積'] = df_x['専有面積'].str.replace("m2","")
  df_x['専有面積'] = df_x['専有面積'].astype(np.float64)

  df_x = df_x.drop(["住所","間取り","全階数","最寄り＿1","字","間取り"],axis=1)

  return df_x,df_y


x,y = data_cleansing("300output.csv")

