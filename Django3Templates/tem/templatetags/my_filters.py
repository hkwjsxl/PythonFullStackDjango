from django import template

register = template.Library()


@register.filter('hide_phone')
def hide_phone(phone):
    if isinstance(phone, int):
        phone = str(phone)
    return phone[:3] + '****' + phone[-4:]
