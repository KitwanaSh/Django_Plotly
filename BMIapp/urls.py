from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'BMIapp'

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),

    path('',
         views.index,
         name='index'),

    path('BMIApp/',
         views.index,
         name='index')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)