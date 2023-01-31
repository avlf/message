from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('name',)

    # def get_fields(self, request, obj=None):
    # pass

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Message, MessageAdmin)
