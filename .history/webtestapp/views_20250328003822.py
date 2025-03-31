from django.shortcuts import render,redirect
from .forms import DataForm
from .utils.summo_calculator import calculate
import pandas as pd
import numpy as np
from django.core.cache import cache

def index(request):
    price = 0
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():  # バリデーションを実行
            initial_data = form.cleaned_data  # 送信されたデータを初期値として使用
            form = DataForm(initial=initial_data)  # 初期値付きの新しいフォームを作成
            
            new_data = pd.DataFrame({
                '築年数': np.int16(initial_data['year']),
                '階': np.int32(initial_data['stairs']),
                '管理費': np.int32(initial_data['fee']),
                '専有面積': np.float64(initial_data['area']),
                '区': pd.Categorical([initial_data['ward'],]),
                '最寄り駅': pd.Categorical([initial_data['station'],]),
                '歩分': np.int64(initial_data['walk']),
                '地下階数': np.int64(initial_data['fullbasement']),
                '地上階数': np.int64(initial_data['fullstairs']),
                '居室': np.int64(initial_data['rooms']),
                'S': np.int64(1 if 'S' in initial_data['sldk'] else 0),
                'L': np.int64(1 if 'L' in initial_data['sldk'] else 0),
                'D': np.int64(1 if 'D' in initial_data['sldk'] else 0),
                'K': np.int64(1 if 'K' in initial_data['sldk'] else 0),
                '賃貸アパート': np.bool_('賃貸アパート' == initial_data['type']),
                '賃貸テラス・タウンハウス': np.bool_('賃貸テラス・タウンハウス' == initial_data['type']),
                '賃貸マンション': np.bool_('賃貸マンション' == initial_data['type']),
                '賃貸一戸建て': np.bool_('賃貸一戸建て' == initial_data['type']),
            })
            
            # print(type(initial_data["ward"]))
            # cache.clear()

            
            
            print(price)
            price = calculate(new_data)
            request.session['price'] = price
            return redirect("result")
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
    

def result(request):
    price = request.session.get('price')
    dic = {"price":price}
    return render(request,"result.html",price)
