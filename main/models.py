from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=90, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Цена")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title