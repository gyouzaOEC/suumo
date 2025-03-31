from .suumo_cleansing import data_cleansing



def calculate():
    df_x,df_y = data_cleansing("/work/django/first/suumo/output_utf-8.csv")
    