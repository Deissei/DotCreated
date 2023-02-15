from django.db import models

class Plan(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='media/logo')
    title = models.CharField(max_length=30, verbose_name='Название Плана')
    description = models.TextField(max_length=250, verbose_name='Описание')
    slug = models.SlugField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'План'
