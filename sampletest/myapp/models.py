from django.db import models
from django.core import validators


class Bb(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость', 
                              validators=[validators.MinValueValidator(0, 'Цена не может быть меньше 0!')])
    published = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, db_index=True)
    rublic = models.ForeignKey('Rublic', on_delete=models.PROTECT, null=True, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']

    def __str__(self):
        return f'{self.title}\n{self.price}'
    

class Rublic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)

    class Meta:
        verbose_name_plural = 'Рубирики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name