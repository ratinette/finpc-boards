from django.contrib import admin

# Register your models here.

from app.models import Dog, DogOwner, Board, Post, Comment

admin.site.register(Dog)
admin.site.register(DogOwner)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
