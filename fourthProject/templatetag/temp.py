from django import template
register = template.Library()

def cut(values,args):
    """
    this is the cut out all  of argsfrom string
    """
    return values.replace(args,'')
register.filter('cut', cut)
    
