from django import template

register=template.Library()

@register.filter('swapping') # considers given name as filter name
def swap(value):
    return value.swapcase()

@register.filter()  #considers function name as filter name
def remove(value,arg):
    return value.replace(arg,'-#-')

@register.filter()
def count(value,arg):
    return value.count(arg)

@register.filter()
def occurance(value,arg):
    d={}
    for i in value:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c

import re
@register.filter()
def regular(value,arg):
    return re.findall(arg,value)



# register.filter('Filter Name',Function Address)
# register.filter('swapping',swap)
# register.filter('removing',remove)