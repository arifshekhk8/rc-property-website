from decimal import Decimal

from django import template

register = template.Library()


@register.filter
def money(value):
    integer = str(int(Decimal(value)))
    tail = integer[-3:]
    rest = integer[:-3]
    groups = []
    while rest:
        groups.insert(0, rest[-2:])
        rest = rest[:-2]
    return "৳" + ",".join(groups + [tail])


@register.filter
def measurement(value):
    number = Decimal(value)
    return (
        f"{number:,.0f}"
        if number == number.to_integral_value()
        else f"{number:,.2f}".rstrip("0").rstrip(".")
    )
