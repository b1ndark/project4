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
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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


class EditProfile(LoginRequiredMixin, UserPassesTestMixin,
                  SuccessMessageMixin, generic.UpdateView):
    """
    Render Edit Profile Page so User can a Edit Profile
    """
    model = UserProfile
    template_name = 'profiles/edit_profile.html'
    fields = ('first_name', 'last_name', 'profile_image', 'car_model',
              'email_address', 'county', 'city', 'postcode', 'country',
              'facebook', 'twitter', 'instagram', 'youtube')

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs['pk'])

        context = {
            "profile": profile,
            'form': EditProfileForm(instance=profile)
        }

        return context
    success_message = "Your Profile has been Updated"


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, generic.DeleteView):
    """
    Render Account delete Page so User can a Delete Account
    and get redirect to Home page
    """
    model = User
    template_name = 'profiles/delete_account.html'

    def test_func(self):
        return self.get_object().profile.user == self.request.user

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs['pk'])

        context = {
            "profile": profile,
            'form': EditProfileForm(instance=profile)
        }

        return context

    success_url = reverse_lazy('home')
    success_message = "Your Account has successfully been Deleted"


def signup(request):
    """
    Signup Template
    """
    if request.user.is_authenticated:
        return redirect('/')

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
