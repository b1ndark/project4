from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import UserProfile
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login


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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'profiles/signup.html', {'form': form})
