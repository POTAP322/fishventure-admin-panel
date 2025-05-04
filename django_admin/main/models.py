from django.db import models

class Players(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    hash_password = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False  #чтобы Django не управлял миграциями для этой таблицы
        db_table = 'Players'

    def __str__(self):
        return self.username

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    log_text = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Logs'

    def __str__(self):
        return f"Log {self.id}"

class PlayerLogs(models.Model):
    id = models.AutoField(primary_key=True)
    Player_id = models.ForeignKey(Players, on_delete=models.CASCADE, db_column='Player_id')
    entered_at = models.DateTimeField()
    exit_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PlayerLogs'

    def __str__(self):
        return f"PlayerLog {self.id}"