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
    
    
    
    
            ype_val = cleaned_data['type']
            ear_val = cleaned_data['year']
            tairs_val = cleaned_data['stairs']
            ee_val = cleaned_data['fee']
            rea_val = cleaned_data['area']
            ard_val = cleaned_data['ward']
            tation_val = cleaned_data['station']
            alk_val = cleaned_data['walk']
            ullbasement_val = cleaned_data['fullbasement']
            ullstairs_val = cleaned_data['fullstairs']
            ooms_val = cleaned_data['rooms']
            ldk_val = cleaned_data['sldk']