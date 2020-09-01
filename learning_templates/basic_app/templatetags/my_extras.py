from django import template

register = template.Library()

# @register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg, '')

#first cut is the string that you call the function when using a templatetag
#second cut is to call the function created above
register.filter('cut', cut)
