from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('typerforum.urls'), name='typerforum_urls'),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('profiles/', include('profiles.urls')),
    # path('contact/', include('contact.urls')),
]
