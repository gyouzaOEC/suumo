from django.shortcuts import render
from .forms import DataForm
from .utils.summo_calculator import calculate
import pandas as pd
import numpy as np

def index(request):
    price = 0
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():  # バリデーションを実行
            initial_data = form.cleaned_data  # 送信されたデータを初期値として使用
            form = DataForm(initial=initial_data)  # 初期値付きの新しいフォームを作成
            
            new_data = pd.DataFrame({
    '築年数': np.int16(ini['year']),
    '階': np.int32(ini['stairs']),
    '管理費': np.int32(ini['fee']),
    '専有面積': np.float64(ini['area']),
    '区': pd.Categorical(ini['ward']),
    '最寄り駅': pd.Categorical(ini['station']),
    '歩分': np.int64(ini['walk']),
    '地下階数': np.int64(cleaned_data['ini']),
    '地上階数': np.int64(cleaned_data['ini']),
    '居室': np.int64(ini['rooms']),
    'S': np.int64(),
    'L': np.int64(),
    'D': np.int64(),
    'K': np.int64(),
    '賃貸アパート': np.bool_(),
    '賃貸テラス・タウンハウス': np.bool_(),
    '賃貸マンション': np.bool_(),
    '賃貸一戸建て': np.bool_(),
})
            price = calculate(new_data)
        else:
            # フォームが無効な場合の処理 (エラーメッセージを表示するなど)
            pass
    else:
        form = DataForm()
        
    my_dict = {
        "forms":form,
        "price":price
    }
    
    return render(request,"index.html",my_dict)
