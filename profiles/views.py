from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import UserProfile
from .forms import SignupForm, ProfileForm, EditProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy


class UserProfiles(TemplateView):
    """
    Profile Template
    """

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs['user'])
        context = {
            "profile": profile,
            'form': ProfileForm(instance=profile)
        }

        return context


def signup(request):
    """
    Signup Template
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Your account has been created and logged in")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Please fill the form correctly")
    else:
        form = SignupForm()

    return render(request, 'profiles/signup.html', {'form': form})


def editProfile(request):
    """
    Edit Template
    """
    form = EditProfileForm(instance=request.user)
    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form = EditProfileForm(instance=request.user)
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Your Profile has been updated")
            return redirect('/')
        else:
            form = EditProfileForm(instance=request.user)
            messages.add_message(request, messages.ERROR,
                                 "Please fill the form correctly")

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'profiles/edit_profile.html', {'form': form})
