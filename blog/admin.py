from django.contrib import admin
from .models import Post, Category, Tag, Comment


# summernote 관련 라이브러리 
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Comment)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)