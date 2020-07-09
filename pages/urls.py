from django.contrib import admin
from django.urls import path

from .views import HomePageView, home_page

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home1/', HomePageView.as_view(), name='home1'),
    path('home2/', home_page, name='home'),
]
