from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    CATEGORY_CHOICES = (
        ('IT', 'IT'),
        ('Art', 'Art'),
        ('Design', 'Design'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Politics', 'Politics'),
        ('Business', 'Business'),
    )

    name = models.CharField(max_length=
                            255, choices=CATEGORY_CHOICES, default='IT')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_date']