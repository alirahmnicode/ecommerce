from django import template

register = template.Library()


def update_params(context, **kwargs):
    query = context["request"].GET.copy()
    for i, v in kwargs.items():
        query[i] = v
    return query.urlencode()


register.simple_tag(update_params, takes_context=True)
