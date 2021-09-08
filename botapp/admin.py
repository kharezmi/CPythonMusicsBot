from django.contrib import admin
from .models import Users, Musics, TaskManager



class MusicsAdmin(admin.ModelAdmin):
    list_display = ['music_name', 'music_id']
    ordering = ['music_name']


admin.site.register(Musics, MusicsAdmin)



class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'u_id']
    ordering = ['name']


admin.site.register(Users, UsersAdmin)


class TaskManagerAdmin(admin.ModelAdmin):

    list_display = ['updated', 'created', 'done', 'date', 'info', ]

admin.site.register(TaskManager, TaskManagerAdmin)