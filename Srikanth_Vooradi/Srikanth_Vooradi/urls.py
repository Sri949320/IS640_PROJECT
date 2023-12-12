from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
# Other imports as needed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ReachOutMe.urls')),
]
