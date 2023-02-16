from django.db import models

class Services(models.Model):
    image = models.ImageField(verbose_name='Лого', upload_to='media/logo')
    title = models.CharField(max_length=30, verbose_name='Название Сервиса')
    description = models.TextField(max_length=50, verbose_name='Описание')
    slug = models.SlugField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Сервисы'

class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_num = models.IntegerField()
    email = models.EmailField(max_length=100)
    adres = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='media/image1')
    image2 = models.ImageField(upload_to='media/image2')
    image3 = models.ImageField(upload_to='media/image3')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контакт'

class Plan(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='media/logo')
    title = models.CharField(max_length=30, verbose_name='Название Плана')
    description = models.TextField(max_length=250, verbose_name='Описание')
    slug = models.SlugField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'План'

class Rewiews(models.Model):
    date = models.DateField()
    text = models.TextField(max_length=300)
    image = models.ImageField(upload_to='movie/image_user', null=True)
    prof = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    deviz = models.TextField(max_length=350, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Отзывы'

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='media/logo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'