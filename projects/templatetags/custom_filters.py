from django import template
"""
to be able to access a particluar list-item in a list of dictionaries. Suggested by ChatGPT 
"""
register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
