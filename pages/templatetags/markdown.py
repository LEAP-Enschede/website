from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(content):
    return md.markdown(content, extensions=['markdown.extensions.fenced_code']).replace('<a', '<a target="_blank"')
