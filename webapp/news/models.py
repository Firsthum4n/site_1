from django.db import models


class Articles(models.Model):
    objects = models.Manager()
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('статья')
    date = models.DateTimeField('Дата публекации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
