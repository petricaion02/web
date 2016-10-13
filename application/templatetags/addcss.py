from django import template
register = template.Library()

@register.simple_tag(name='add_args')
def addcss(field, **kwargs):
   return field.as_widget(attrs=kwargs)
