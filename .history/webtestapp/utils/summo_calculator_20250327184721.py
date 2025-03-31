from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd
import numpy as np


def calculate(new_data):
    df_x,df_y = pd.read_csv("/work/django/first/suumo/x.csv"),\
        pd.read_csv("/work/django/first/suumo/y.csv")
    
    model = lgb.LGBMRegressor(max_bin=1024)
    x['区'] = x['区'].astype('category')
    x['最寄り駅'] = x['最寄り駅'].astype('category')
    model.fit(x, y, categorical_feature=['区','最寄り駅'])

    new_data['区'] = new_data['区'].astype('category')
    new_data['最寄り駅'] = new_data['最寄り駅'].astype('category')
    pred = model.predict(new_data)
    print(pred)
