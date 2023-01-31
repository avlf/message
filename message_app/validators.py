from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'[+]\d{1,3}[(]\d{3}[)]\d{3}[-]\d{2}[-]\d{2}',
    message=_('Use correct phone number.'),
    code='invalid_regex'
)
