from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext as _

from .forms import MessageForm


def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            intance = form.save()
            messages.success(request, _('Message is succesfully sent'))
        else:
            messages.error(request, _('Invalid form'), extra_tags='danger')

    else:
        form = MessageForm()

    return render(
        request=request,
        template_name='message_app/message_form.html',
        context={
            'form': form,
        },

    )

