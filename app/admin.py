from django.contrib import admin
from .models import Model_test, mangaModel, animeModel, loveModel, sportsModel

# Register your models here.
admin.site.register(Model_test)
admin.site.register(mangaModel)
admin.site.register(animeModel)
admin.site.register(loveModel)
admin.site.register(sportsModel)