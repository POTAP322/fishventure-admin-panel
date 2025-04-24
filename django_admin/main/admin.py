from django.contrib import admin
from .models import Players, Logs, PlayerLogs

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at')
    search_fields = ('username',)

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_text', 'created_at')
    list_filter = ('created_at',)

@admin.register(PlayerLogs)
class PlayerLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Players_id', 'entered_at', 'exit_at')
    list_filter = ('Players_id', 'created_at')