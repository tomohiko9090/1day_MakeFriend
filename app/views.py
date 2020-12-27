from django.views.generic.detail import DetailView
# from todo_herokuapp.models import TodoModel
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from .models import TodoModel
from .models import *
from django.urls import reverse_lazy
# Create your views here.

def test(request):
    return render(request, 'test.html')

# ホーム
def home(request):
    return render(request, 'home.html')

# 作成
class create(CreateView):
    template_name = 'create.html'
    model = Model_test
    # フィールドを指定する
    fields = ('text',)
    # データの作成が完了したときに遷移するURLを指定する
    # viewを指定して、それに関連するURLに飛ぶ
    success_url = reverse_lazy('home')

# マンガ
def manga(request):
    return render(request, 'manga.html')
# class manga(ListView):
#     # htmlを呼び出す
#     template_name = 'manga.html'
#     # 使うデータを指定する
#     model = mangaModel

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