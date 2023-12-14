from django.contrib import admin
from .models import UserContact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )


admin.site.register(UserContact, ContactAdmin)
