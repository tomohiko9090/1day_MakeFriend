from django.db import models

class Model_test(models.Model):
    author = models.CharField(max_length=100, null=True) # 投稿者
    title = models.CharField(max_length=100)
    content = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

# マンガ
class mangaModel(models.Model):
    author = models.CharField(max_length=100, null=True) # 投稿者
    title = models.CharField(max_length=100)
    content = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

# アニメ
class animeModel(models.Model):
    author = models.CharField(max_length=100, null=True) # 投稿者
    title = models.CharField(max_length=100)
    content = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

# 恋愛
class loveModel(models.Model):
    author = models.CharField(max_length=100, null=True) # 投稿者
    title = models.CharField(max_length=100)
    content = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

# スポーツ
class sportsModel(models.Model):
    author = models.CharField(max_length=100, null=True) # 投稿者
    title = models.CharField(max_length=100)
    content = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

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