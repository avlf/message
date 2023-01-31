from django.db import models
from django.utils.translation import gettext as _

from message_app.validators import phone_validator


class Message(models.Model):
    class ErrorType(models.TextChoices):
        DESCRIPTION_ERROR = 'DE', _('Description error')
        COMBAT_DATA_ERROR = 'CDE', _('Combat data error')
        NAME_ERROR = 'NE', _('Name error')
        IMG_ERROR = 'IE', _('Image error')
        FRONT_DISPLAY_ERROR = 'FDE', _('Front display error')
        OTHER_ERROR = 'OE', _('Other error')

    name = models.CharField(_('Name'), max_length=200)
    phone = models.CharField(_('Phone'), max_length=20, validators=[phone_validator])
    email = models.EmailField(_('Email'))
    type_error = models.CharField(_('Type'), max_length=200, choices=ErrorType.choices, default=ErrorType.OTHER_ERROR)
    text_error = models.CharField(_('Text'), max_length=202)

    def __str__(self):
        return f'message from {self.name}'
