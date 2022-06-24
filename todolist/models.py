from django.db import models

# Create your models here.
STATUS_CODE = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    task = models.CharField(max_length=50, null=False, blank=False, verbose_name="Задача")
    status = models.CharField(max_length=20, choices=STATUS_CODE, verbose_name="Статус", default=STATUS_CODE[0][0])
    created_at = models.DateField(default="", verbose_name="Дедлайн")

    def __str__(self):
        return f"{self.id}. {self.task}: {self.status}"

    class Meta:
        db_table = "Tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
