from django.contrib import admin
from .models import Post, Category

# 管理画面からデータベースを操作するための記述
admin.site.register(Post)
admin.site.register(Category)