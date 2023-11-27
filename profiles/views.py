from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import UserProfile
from .forms import SignupForm, ProfileForm, EditProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class UserProfiles(TemplateView):
    """
    Profile Template
    """

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs['pk'])
        context = {
            "profile": profile,
            'form': ProfileForm(instance=profile)
        }

        return context


class EditProfile(SuccessMessageMixin, generic.UpdateView):
    """
    Render Edit Profile Page so User can a Edit Profile
    """
    model = UserProfile
    template_name = 'profiles/edit_profile.html'
    fields = ('first_name', 'last_name', 'profile_image', 'car_model',
              'user_email', 'county', 'city', 'postcode', 'country',)

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs['pk'])

        context = {
            "profile": profile,
            'form': EditProfileForm(instance=profile)
        }

        return context
    success_message = "Your Profile has been Updated"


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
