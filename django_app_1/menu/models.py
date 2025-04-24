from django.db import models


class Menu(models.Model):
    '''Храним имена и уникальные идентификаторы меню.'''

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)


class MenuItem(models.Model):
    '''Храним сами модели.
    Каждое меню может быть подменю другого меню, поэтому
    есть ссылка на родительское меню.
    Сущности будут ссылаться на другие сущности в таблице.
    По принципу многие к одному??
    Дочерние меню могут ссылаться все на одно родительское.'''

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'MenuItem',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
