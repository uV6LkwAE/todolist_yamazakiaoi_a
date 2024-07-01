
# your_app_name/templatetags/custom_filters.py
from django import template
from datetime import date

register = template.Library()

@register.filter
def days_until(target_date):
    if not isinstance(target_date, date):
        return ''
    today = date.today()
    delta = target_date - today
    if delta.days >= 0:
        return f'{delta.days}日'
    else:
        return '期限が過ぎています'
