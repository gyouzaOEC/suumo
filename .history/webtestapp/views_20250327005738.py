from django.shortcuts import render
from .forms import DataForm
from .utils.summo_calculator import calculate

def index(request):
    price = 0
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():  # バリデーションを実行
            initial_data = form.cleaned_data  # 送信されたデータを初期値として使用
            form = DataForm(initial=initial_data)  # 初期値付きの新しいフォームを作成
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
