from django.shortcuts import render
from django.views.generic import View
from .models import Post

# Viewを継承して、クラスベース汎用ビューを作成
class IndexView(View):
  def get(self, request, *args, **kwargs):       # get関数は画面が表示されたら必ず最初に呼ばれる
    post_data = Post.objects.order_by('-id')     # Postモデルを呼び出し、降順に並び替えている
    return render(request, 'app/index.html', {   # render関数を使用して、テンプレートにデータを渡します
      'post_data': post_data,
    })