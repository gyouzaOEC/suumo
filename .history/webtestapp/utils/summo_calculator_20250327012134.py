from .suumo_cleansing import data_cleansing
import lightgbm as lgb
import pandas as pd


def calculate(new_data):
    df_x,df_y = data_cleansing("/work/django/first/suumo/output_utf-8.csv")
    
    model = lgb.LGBMRegressor(max_bin=1024)
    model.fit(df_x, df_y, categorical_feature=['区','最寄り駅']])

    
    new_data['区'] = new_data['区'].astype('category')
    new_data['最寄り駅'] = new_data['最寄り駅'].astype('category')
    pred = model.predict(new_data)
    
    
    
    
            type_val = cleaned_data['type']
            year_val = cleaned_data['year']
            stairs_val = cleaned_data['stairs']
            fee_val = cleaned_data['fee']
            area_val = cleaned_data['area']
            ward_val = cleaned_data['ward']
            station_val = cleaned_data['station']
            walk_val = cleaned_data['walk']
            fullbasement_val = cleaned_data['fullbasement']
            fullstairs_val = cleaned_data['fullstairs']
            rooms_val = cleaned_data['rooms']
            sldk_val = cleaned_data['sldk']