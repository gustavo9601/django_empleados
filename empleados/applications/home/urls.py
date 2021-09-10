from django.urls import path
from .views import HomeView, HomeListView

urls_home = [
    path('home/', HomeView.as_view()),
    path('list/', HomeListView.as_view()),
]