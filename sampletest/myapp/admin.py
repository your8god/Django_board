from django.contrib import admin

from .models import Bb, Rublic

class BbAdmin(admin.ModelAdmin):
    list_display = ('rublic', 'title', 'content', 'price', 'published')
    search_fields = ('title', 'content', 'rublic')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rublic)