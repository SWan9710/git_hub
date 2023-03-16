from django.urls import path
from . import views
# from . >> 내 위치에서 import views >> views를 가져옴

urlpatterns = [
   path('hello/<str:name>/', views.hello),
]
