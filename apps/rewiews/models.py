from django.db import models

class Rewiews(models.Model):
    date = models.DateField()
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Отзывы'