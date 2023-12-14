from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import UserContact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    """
    Contact Template
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                f"Message from {form.cleaned_data['name']}"
                f"Email: <{form.cleaned_data['email']}>\n\n",
                f"Message:\n{form.cleaned_data['message']}",
                None,
                ['typer9000@example.com'],
            )

            messages.add_message(request, messages.SUCCESS,
                                 "Your Form has been submited,\
                                     we will reply shortly")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Please fill the form correctly")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
