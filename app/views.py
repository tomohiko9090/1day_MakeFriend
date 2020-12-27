from django.views.generic.detail import DetailView
# from todo_herokuapp.models import TodoModel
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from .models import TodoModel
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
    return render(request, 'test.html')

# 会員登録
def signupfunc(request):
    # キーを使って特定のデータを抽出する(get)
    user2 = User.objects.get(username='wata')
    print(user2)
    if request.method == 'POST': # usernameとパスワードを入力した後に呼ばれたとき
        # 入力されたデータを変数に格納する
        username2 = request.POST['username']
        password2 = request.POST['password']

        # try, exceptはエラーの処理に使う
        try:
            # 入力されたusernameと同じものが既にあったら取ってくる
            User.objects.get(username=username2)
            # エラーを出して、登録しない
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        # tryが失敗したときに実行される
        except:
            # ユーザーを作成する
            # usernameが被っていなければ登録する
            # (ユーザー名, eメール, パスワード)
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'login.html', {'some':100})

    # {'変数名':htmlファイルに代入するデータ}
    return render(request, 'signup.html', {'some':100})

# ログイン
def loginfunc(request):
    if request.method == 'POST': # usernameとパスワードを入力した後に呼ばれたとき
        # データを引っ張ってきて変数に格納する
        username2 = request.POST['username'] # 入力されたusername
        password2 = request.POST['password'] # 入力されたパスワード
        # ユーザーの認証
        user = authenticate(request, username=username2, password=password2)

        if user is not None: # 認証されたユーザーがいるとき
            # ログインする
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')

# ログインしていなければsettings.pyのLOGIN_URLに飛ぶ
@login_required
# ホーム
def home(request):
    # return render(request, 'home.html')
    # ログインしている人のユーザー名を取得する
    username = request.user.get_username()
    return render(request, 'home.html', {'username':username})

# マンガ作成
class manga_create(CreateView):
    template_name = 'manga_create.html'
    model = mangaModel
    # フィールドを指定する
    fields = ('title','content','author')
    # データの作成が完了したときに遷移するURLを指定する
    # viewを指定して、それに関連するURLに飛ぶ
    success_url = reverse_lazy('manga')

# マンガ
class manga(ListView):
    # htmlを呼び出す
    template_name = 'manga.html'
    # 使うデータを指定する
    model = mangaModel

# マンガ詳細
def manga_detailfunc(request, pk):
    # データの取得
    object = mangaModel.objects.get(pk=pk)
    return render(request, 'manga_detail.html', {'object':object})

# アニメ作成
class anime_create(CreateView):
    template_name = 'anime_create.html'
    model = animeModel
    # フィールドを指定する
    fields = ('title','content','author')
    # データの作成が完了したときに遷移するURLを指定する
    # viewを指定して、それに関連するURLに飛ぶ
    success_url = reverse_lazy('anime')

# アニメ
class anime(ListView):
    # htmlを呼び出す
    template_name = 'anime.html'
    # 使うデータを指定する
    model = animeModel

# アニメ詳細
def anime_detailfunc(request, pk):
    # データの取得
    object = animeModel.objects.get(pk=pk)
    return render(request, 'anime_detail.html', {'object':object})

# 恋愛作成
class love_create(CreateView):
    template_name = 'love_create.html'
    model = loveModel
    # フィールドを指定する
    fields = ('title','content','author')
    # データの作成が完了したときに遷移するURLを指定する
    # viewを指定して、それに関連するURLに飛ぶ
    success_url = reverse_lazy('love')

# 恋愛
class love(ListView):
    # htmlを呼び出す
    template_name = 'love.html'
    # 使うデータを指定する
    model = loveModel

# 恋愛詳細
def love_detailfunc(request, pk):
    # データの取得
    object = loveModel.objects.get(pk=pk)
    return render(request, 'love_detail.html', {'object':object})

# スポーツ作成
class sports_create(CreateView):
    template_name = 'sports_create.html'
    model = sportsModel
    # フィールドを指定する
    fields = ('title','content','author')
    # データの作成が完了したときに遷移するURLを指定する
    # viewを指定して、それに関連するURLに飛ぶ
    success_url = reverse_lazy('sports')

# スポーツ
class sports(ListView):
    # htmlを呼び出す
    template_name = 'sports.html'
    # 使うデータを指定する
    model = sportsModel

# スポーツ詳細
def sports_detailfunc(request, pk):
    # データの取得
    object = sportsModel.objects.get(pk=pk)
    return render(request, 'sports_detail.html', {'object':object})

# ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')

# # ListViewを使う
# class TodoList(ListView):
#     # htmlを呼び出す
#     template_name = 'list.html'
#     # 使うデータを指定する
#     model = TodoModel

# # DetailViewを使う
# class TodoDetail(DetailView):
#     template_name = 'detail.html'
#     model = TodoModel

# # CreateViewを使う
# class TodoCreate(CreateView):
#     template_name = 'create.html'
#     model = TodoModel
#     # フィールドを指定する
#     fields = ('title', 'memo', 'priority', 'duedate')
#     # データの作成が完了したときに遷移するURLを指定する
#     # viewを指定して、それに関連するURLに飛ぶ
#     success_url = reverse_lazy('list')

# # DeleteViewを使う
# class TodoDelete(DeleteView):
#     template_name = 'delete.html'
#     model = TodoModel
#     # データの作成が完了したときに遷移するURLを指定する
#     # viewを指定して、それに関連するURLに飛ぶ
#     success_url = reverse_lazy('list')

# # UpdateViewを使う
# class TodoUpdate(UpdateView):
#     template_name = 'update.html'
#     model = TodoModel
#     fields = ('title', 'memo', 'priority', 'duedate')
#     success_url = reverse_lazy('list')