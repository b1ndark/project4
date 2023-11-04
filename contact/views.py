from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserContact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    Contact Template
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,
                                 "Your Form has been submited, we will reply shortly")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Please fill the form correctly")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
