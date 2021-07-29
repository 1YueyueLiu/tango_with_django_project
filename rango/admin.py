from rango.models import Page
from django.contrib import admin
from rango.models import Category


class PageAdmin(admin.ModelAdmin):
      list_disaplay = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

