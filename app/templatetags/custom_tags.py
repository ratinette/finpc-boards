from datetime import datetime, timedelta

from django import template
from django.utils import timezone

register = template.Library()


@register.filter()
def word_changer(value):
    value = str(value).lower()
    if value == "python":
        return "Java"
    elif value == "java":
        return "Python"
    return value


@register.filter
def time_since(value):
    now = timezone.now()
    diff = now - value

    if diff < timedelta(minutes=1):
        return "방금 전"
    elif diff < timedelta(minutes=60):
        minutes = int(diff.seconds / 60)
        return f"{minutes}분 전"
    else:
        return value.strftime("%Y년 %m월 %d일 %H:%M:%S")
