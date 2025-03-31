import pandas as pd
import lightgbm as lgb
import joblib

def predict_rent(district, station, size):
    # モデル読み込み（事前に訓練済み）
    model = joblib.load('path/to/trained_model.pkl')
    
    # 入力データをDataFrameに
    data = pd.DataFrame({
        'district': [district],
        'station': [station],
        'size': [size]
    })
    
    # 予測
    pred = model.predict(data)
    return pred[0]