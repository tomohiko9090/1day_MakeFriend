from django.contrib import admin
from django.urls import path, include
from .views import test, home, create, manga
# from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('test/', test, name='test'),
    # ホーム
    path('home/', home, name='home'),
    # 作成画面
    path('create/', create.as_view(), name='create'),
    # マンガ
    path('manga/', manga, name='manga'),
    # アニメ
    # path('anime', anime, )

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
