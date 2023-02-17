from django.db import models
from django.shortcuts import reverse


class Author(models.Model):
    image = models.ImageField(upload_to='media/blog/author')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Пользователи'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/blog')
    create_add = models.DateField()
    desc = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'Блог'
    
class Comment(models.Model):
    fullname = models.CharField(max_length=80)
    email = models.EmailField()
    create_add = models.DateField(auto_now_add=True)
    comment = models.TextField(max_length=120)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.fullname} | {self.create_add}"

    class Meta:
        verbose_name_plural = "Коментарии"