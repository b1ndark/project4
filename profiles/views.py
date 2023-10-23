from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserProfile
from .forms import ProfileForm


class UserProfiles(TemplateView):
    """
    Profile Template
    """

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = UserProfile.objects.get(user=self.kwargs["user"])
        context = {
            "profile": profile,
            'form': ProfileForm(instance=profile)
        }

        return context
