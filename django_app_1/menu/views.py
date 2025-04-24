from django.shortcuts import render


def menu(request):
    template_name = 'menu/menu_template.html'
    return render(request, template_name=template_name)