"""
from django.shortcuts import render
from .views import HomePageView

# Create your views here.

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
"""

from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'home.html'


def home_page(request):
    #messages.warning(request, 'Message' )
    return render(request, "home.html")
