from django import template
from ..models import Menu


register = template.Library()


@register.simple_tag
def draw_menu(name):
    menu = Menu.objects.prefetch_related('menuitem_set').get(name=name)
    return menu