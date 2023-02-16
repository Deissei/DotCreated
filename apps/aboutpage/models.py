from django.db import models


class AboutModels(models.Model):
    image = models.ImageField(upload_to='media/about')
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О нас'
