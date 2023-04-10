from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200, verbose_name="Название")
    sud_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name="Описание")
    body = models.TextField(null=True, blank=True, verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name="Избранные")
    tags = models.ManyToManyField(Tag, verbose_name="Направление")
    image = models.ImageField(null=True, blank=True, upload_to='images', default='1.jpg', verbose_name="Изображение")

    def __str__(self) -> str:
        return self.headline
