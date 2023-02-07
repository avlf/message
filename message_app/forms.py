from django import forms
from django.utils.translation import gettext as _

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'name',
            'phone',
            'email',
            'type_error',
            'text_error'
        )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Max')}),
            'phone': forms.TextInput(attrs={'placeholder': '+7(858)855-95-95'}),
            'email': forms.TextInput(attrs={'placeholder': 'hgh@gmail.com'}),
            'text_error': forms.Textarea(attrs={'placeholder': _('All error text')}),
        }

    # def save(self, commit=True):
    # pass
