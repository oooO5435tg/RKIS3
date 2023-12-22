from django.contrib import admin

from whiteboard.models import MyUser, Comment, Post

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Comment)
admin.site.register(Post)
