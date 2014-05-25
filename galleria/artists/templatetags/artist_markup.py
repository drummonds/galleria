from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

import markdown2 as md2

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown2(value):
    extensions = ["nl2br","wiki-tables", ]

    return mark_safe(md2.markdown(force_str(value),extras=extensions,safe_mode=True))
