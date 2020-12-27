from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfunc, test, home, manga_create, manga, manga_detailfunc, anime, anime_create, anime_detailfunc, love, love_create, love_detailfunc, sports, sports_create, sports_detailfunc, logoutfunc
# from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('test/', test, name='test'),
    # 会員登録画面
    path('', signupfunc, name='first'),
    # 会員登録画面
    path('signup/', signupfunc, name='signup'),
    # ログイン画面
    path('login/', loginfunc, name='login'),
    # ログアウト
    path('logout/', logoutfunc, name='logout'),
    # ホーム
    path('home/', home, name='home'),
    # マンガ
    path('manga/', manga.as_view(), name='manga'),
    # マンガ作成
    path('manga_create/', manga_create.as_view(), name='manga_create'),
    # マンガ詳細
    path('manga_detail/<int:pk>', manga_detailfunc, name='manga_detail'),
    # アニメ
    path('anime/', anime.as_view(), name='anime'),
    # アニメ作成
    path('anime_create/', anime_create.as_view(), name='anime_create'),
    # アニメ詳細
    path('anime_detail/<int:pk>', anime_detailfunc, name='anime_detail'),
    # 恋愛
    path('love/', love.as_view(), name='love'),
    # 恋愛作成
    path('love_create/', love_create.as_view(), name='love_create'),
    # 恋愛詳細
    path('love_detail/<int:pk>', love_detailfunc, name='love_detail'),
    # スポーツ
    path('sports/', sports.as_view(), name='sports'),
    # スポーツ作成
    path('sports_create/', sports_create.as_view(), name='sports_create'),
    # スポーツ詳細
    path('sports_detail/<int:pk>', sports_detailfunc, name='sports_detail'),

    # path('', TodoList.as_view(), name='list'),
    # # クラスを呼び出すときは.as_view()をつける
    # path('list/', TodoList.as_view(), name='list'),
    # # primary key(pk)を指定して設定する
    # path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    # # 作成画面
    # path('create/', TodoCreate.as_view(), name='create'),
    # # 削除
    # # primary key(pk)(消すデータ)を指定して設定する
    # path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    # # 更新
    # path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
