from django import template
from lists import models as lists_models


register = template.Library()


@register.simple_tag(takes_context=True)
def on_list(context):
    user = context.request.user
    all_items = lists_models.List.objects.filter(user=user).count()
    return all_items
