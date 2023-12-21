from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
