from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd
import numpy as np


def calculate():
    df_x,df_y = data_cleansing("/work/django/first/suumo/output_utf-8.csv")
    
    model = lgb.LGBMRegressor(max_bin=1024)
    model.fit(df_x, df_y, categorical_feature=['区','最寄り駅']])

    new_data = pd.DataFrame({
    '築年数': np.int16,
    '階': np.int32,
    '管理費': np.int32,
    '専有面積': np.float64(50,
    '賃貸アパート': np.bool_,
    '賃貸テラス・タウンハウス': np.bool_,
    '賃貸マンション': np.bool_,
    '賃貸一戸建て': np.bool_,
    '区': pd.Categorical,
    '最寄り駅': pd.Categorical,
    '歩分': np.int64,
    '地下階数': np.int64,
    '地上階数': np.int64,
    '居室': np.int64,
    'S': np.int64,
    'L': np.int64,
    'D': np.int64,
    'K': np.)
})
    new_data['区'] = new_data['区'].astype('category')
    new_data['最寄り駅'] = new_data['最寄り駅'].astype('category')
    pred = model.predict(new_data)