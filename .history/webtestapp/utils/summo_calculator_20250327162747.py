from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd


def calculate(new_data):
    df_x,df_y = pd.read_csv("/work/django/first/suumo/output_utf-8.csv")
    
    model = lgb.LGBMRegressor(max_bin=1024)
    df_x['区'] = df_x['区'].astype('category')
    df_x['最寄り駅'] = df_x['最寄り駅'].astype('category')
    model.fit(df_x, df_y)

    
    new_data['区'] = new_data['区'].astype('category')
    new_data['最寄り駅'] = new_data['最寄り駅'].astype('category')
    pred = model.predict(new_data)
    
    return round(pred,2)
