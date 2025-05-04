from django.contrib import admin
from .models import Players, Logs, PlayerLogs

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at', 'birth_date', 'hash_password','auth_token')
    search_fields = ('username',)

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_text', 'created_at')
    list_filter = ('created_at',)

@admin.register(PlayerLogs)
class PlayerLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Player_id', 'entered_at', 'exit_at')
    list_filter = ('Player_id', 'entered_at',)