"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path


def home(request):
    messages.error(request, "Hello world")
    return redirect("/foobar/")


def foobar(request):
    msgs = ", ".join(message.message for message in messages.get_messages(request))
    return HttpResponse(f"Messages: {msgs}")


urlpatterns = [
    path("", home),
]

urlpatterns += i18n_patterns(
    path("foobar/", foobar),
)
