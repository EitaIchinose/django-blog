from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Viewを継承して、クラスベース汎用ビューを作成
class IndexView(View):
  def get(self, request, *args, **kwargs):       # get関数は画面が表示されたら必ず最初に呼ばれる
    post_data = Post.objects.order_by('-id')     # Postモデルを呼び出し、降順に並び替えている
    return render(request, 'app/index.html', {   # render関数を使用して、テンプレートにデータを渡します
      'post_data': post_data,
    })
    
class PostDetailView(View):
    def get(self, request, *args, **kwargs):
      post_data = Post.objects.get(id=self.kwargs['pk'])
      return render(request, 'app/post_detail.html', {
        'post_data': post_data,
      })
      
class CreatePostView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)
    
    return render(request, 'app/post_form.html', {
      'form': form
    })
    
  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)
    
    if form.is_valid():  # フォームの内容を確認
      post_data = Post() # Postモデルをpost_dataへ格納
      post_data.author = request.user  # ログインユーザーをauthorへ代入
      post_data.title = form.cleaned_data['title']     # フォームで入力されたタイトルのデータを代入
      post_data.content = form.cleaned_data['content'] # フォームで入力された内容のデータを代入
      post_data.save()   # データベースへ保存
      return redirect('post_detail', post_data.id)     # 詳細画面へリダイレクト
    
    return render(request, 'app/post_form.html', {
      'form': form
    })