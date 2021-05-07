from django import template
import datetime
from django.utils import timezone

register = template.Library()

@register.filter
def timer(value):
    time_now = timezone.now()
    total_secs = (time_now - value).total_seconds()
    return total_secs/3600

@register.filter
def splitter(value):
    ls = value.split(',')
    return ls