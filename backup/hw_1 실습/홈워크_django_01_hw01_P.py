from django.urls import path
from my_app import views

# my_pjt/urls.py
# my_app/views.py
urlpatterns = [
    path('hello/', viesw.hello)
]