from django.contrib import admin
from django.urls import include, path
from cofferupApp.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cofferupApp.urls')),
]