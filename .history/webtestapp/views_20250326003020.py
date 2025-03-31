from django.shortcuts import render,redirect
from .forms import DataForm

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():  # バリデーションを実行
            
            return redirect('detail_view', id=data['id'])
        else:
            # フォームが無効な場合の処理 (エラーメッセージを表示するなど)
            pass
    else:
        form = DataForm()
    my_dict = {
        "forms":DataForm(),
        "price":0
    }
    return render(request,"index.html",my_dict)
