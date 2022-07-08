from django.db import models

class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    tasks = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обмен'
        verbose_name_plural = 'Обмены'