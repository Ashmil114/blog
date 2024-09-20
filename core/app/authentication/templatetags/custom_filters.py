from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(value, arg):
    return value.as_widget(attrs={"class": arg})


@register.filter
def truncate_title(value):
    words = value.split()
    if len(words) > 12:
        return " ".join(words[:12]) + "..."
    return value
