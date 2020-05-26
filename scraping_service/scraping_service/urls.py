from django.contrib import admin
from django.urls import path
from .views import home
from scraping.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('qs/', home_view, name='home_view'),

]
