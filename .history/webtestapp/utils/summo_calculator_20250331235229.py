from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd
import numpy as np


def calculate(new_data):
    df_x,df_y = pd.read_csv("/work/django/first/suumo/x.csv"),\
        pd.read_csv("/work/django/first/suumo/y.csv")
    
    model = lgb.LGBMRegressor(max_bin=1024)
    df_x['区'] = df_x['区'].astype('category')
    df_x['最寄り駅'] = df_x['最寄り駅'].astype('category')
    model.fit(df_x, df_y, categorical_feature=['区','最寄り駅'])

    # new_data = pd.DataFrame({
    # '築年数': np.int16(1),
    # '階': np.int32(1),
    # '管理費': np.int32(1),
    # '専有面積': np.float64(1),
    # '賃貸アパート': np.bool_(True),
    # '賃貸テラス・タウンハウス': np.bool_(False),
    # '賃貸マンション': np.bool_(False),
    # '賃貸一戸建て': np.bool_(False),
    # '区': pd.Categorical(['渋谷区']),
    # '最寄り駅': pd.Categorical(['渋谷駅']),
    # '歩分': np.int64(1),
    # '地下階数': np.int64(1),
    # '地上階数': np.int64(1),
    # '居室': np.int64(1),
    # 'S': np.int64(0),
    # 'L': np.int64(0),
    # 'D': np.int64(0),
    # 'K': np.int64(1)
    # })
    
    # new_data['区'] = new_data['区'].astype('category')
    # new_data['最寄り駅'] = new_data['最寄り駅'].astype('category')
    pred = model.predict(new_data)
    return round(pred[0],2)
