from django.urls import path, include, re_path
from .views import ContactsViev


urlpatterns = [
    path('',ContactsViev.as_view(), name='con'),


]
