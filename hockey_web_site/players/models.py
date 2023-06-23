from django.db import models
from django.urls import reverse


CHOICES = [
        ('Левый', 'Левый'),
        ('Правый', 'Правый'),
    ]


class Players(models.Model):
    name = models.TextField(max_length=255, verbose_name='Имя')
    surname = models.TextField(max_length=255, verbose_name='Фамилия')
    number = models.IntegerField(verbose_name='Номер игрока')
    photo = models.ImageField(
        upload_to="photos/players/%Y/%m/%d",
        verbose_name='Фото',
    )
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='Амплуа',
    )
    country = models.TextField(blank=False, verbose_name='Страна')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        verbose_name='Вес'
    )
    age = models.IntegerField(verbose_name='Возраст')
    grip = models.TextField(
        choices=CHOICES,
        default='Левый',
        verbose_name='Хват'
    )
    content = models.TextField(blank=True, verbose_name='Биография')
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse("player", kwargs={"player_id": self.pk})

    class Meta:
        verbose_name = 'Игрока'
        verbose_name_plural = 'Игроки'
        ordering = ['-time_create', 'name']


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Амплуа'
        verbose_name_plural = 'Амплуа'
        ordering = ['pk']
