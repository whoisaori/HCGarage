from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'time_create',
        'get_html_photo',
        'is_published'
    )
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    search_fields = ('title', 'content')
    empty_value = '-пусто-'
    fields = (
        'title',
        'cat',
        'content',
        'photo',
        'get_html_photo',
        'is_published',
        'time_create',
        )
    readonly_fields = ('time_create', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    empty_value = '-пусто-'
    prepopulated_fields = {'slug': ('name', )}


admin.site.site_title = 'Админ-панель сайта хоккейного клуба Garage'
admin.site.site_header = 'Админ-панель сайта хоккейного клуба Garage'
