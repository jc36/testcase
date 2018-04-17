from django.contrib import admin
from tcase.models import Post, Like


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Like, LikeAdmin)
