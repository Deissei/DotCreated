from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='media/logo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
