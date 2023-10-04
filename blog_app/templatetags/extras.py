from django import template

register=template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    # The `return dict.get(key)` statement is returning the value associated with the specified key in
    # the given dictionary. If the key is not found in the dictionary, it will return `None` by
    # default.
    return dict.get(key)