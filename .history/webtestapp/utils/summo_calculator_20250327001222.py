from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd



def calculate():
    df_x,df_y = data_cleansing("/work/django/first/suumo/output_utf-8.csv")
    
    model = lgb.LGBMRegressor()
    model.fit(df_x, df, categorical_feature=['district'])
