from django.db import models

class Model_test(models.Model):
    text = models.CharField(max_length=100)

class mangaModel(models.Model):
    text = models.CharField(max_length=100)
# class TodoModel(models.Model):
#     # CharField: 文字列を入れるフィールド
#     title = models.CharField(max_length=100)
#     # TextField: 長い文字列を入れるフィールド
#     memo = models.TextField()
#     # 優先度
#     priority = models.CharField(
#         max_length = 50,
#         # 選択肢を表示する
#         choices = PRIORITY
#     )
#     # 日付
#     duedate = models.DateField()
#     # オブジェクトを文字列に変えて表示する
#     def __str__(self):
#         # オブジェクトのタイトルを表示する
#         return self.title