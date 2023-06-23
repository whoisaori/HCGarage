from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Players, Category


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'surname',
        'get_html_photo',
        'grip'
    )
    list_display_links = ('id', 'name', 'surname')
    list_editable = ('grip',)
    list_filter = ('name', 'surname', 'time_create')
    search_fields = ('name', 'surname')
    empty_value = '-пусто-'
    fields = (
        'name',
        'surname',
        'cat',
        'number',
        'photo',
        'get_html_photo',
        'grip',
        'country',
        'height',
        'weight',
        'age',
        'content',
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
