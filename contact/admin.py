from django.contrib import admin
from .models import UserContact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'car_model',
        'message_content',
    )


admin.site.register(UserContact, ContactAdmin)
