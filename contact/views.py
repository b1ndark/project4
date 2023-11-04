from django.shortcuts import render
from django.views.generic import TemplateView


class UserContact(TemplateView):
    """
    Contact Template
    """

    template_name = "contact/contact.html"
