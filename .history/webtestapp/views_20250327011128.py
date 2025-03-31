from django.shortcuts import render
from .forms import DataForm
from .utils.summo_calculator import calculate
from pandas import import pdb; pdb.set_trace()
def index(request):
    price = 0
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():  # バリデーションを実行
            initial_data = form.cleaned_data  # 送信されたデータを初期値として使用
            form = DataForm(initial=initial_data)  # 初期値付きの新しいフォームを作成
            new_data = pd.DataFrame({
    '築年数': np.int16(),
    '階': np.int32(),
    '管理費': np.int32(),
    '専有面積': np.float64(),
    '賃貸アパート': np.bool_(),
    '賃貸テラス・タウンハウス': np.bool_(),
    '賃貸マンション': np.bool_(),
    '賃貸一戸建て': np.bool_(),
    '区': pd.Categorical(),
    '最寄り駅': pd.Categorical(),
    '歩分': np.int64(),
    '地下階数': np.int64(),
    '地上階数': np.int64(),
    '居室': np.int64(),
    'S': np.int64(),
    'L': np.int64(),
    'D': np.int64(),
    'K': np.int64(),
})
            price = calculate(request)
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
