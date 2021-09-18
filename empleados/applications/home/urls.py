from django.urls import path
from .views import HomeView, HomeListView, HomeListTestView, HomeCreateView

urls_home = [
    path('home/', HomeView.as_view()),
    path('list/', HomeListView.as_view()),
    path('test-list/', HomeListTestView.as_view()),
    path('create-home/', HomeCreateView.as_view(), name='home_create'),
]
