from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def price_validator(price):
    if price <= 0.0:
        raise ValidationError(
            _('%(value)s is not a valid price'),
            params={'value': price}
        )
