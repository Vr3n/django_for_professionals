from django.urls import path, re_path
from .views import home_page_view


urlpatterns = [
    path('', home_page_view, name='home')
]