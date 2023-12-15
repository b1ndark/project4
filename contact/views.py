from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import UserContact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    Contact Template
    """
    return render(request, 'contact/contact.html')
