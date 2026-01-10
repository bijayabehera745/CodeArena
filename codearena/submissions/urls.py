from django.urls import path
from .views import submission_success
from .views import submission_success, leaderboard

urlpatterns = [
    path('success/', submission_success, name='submission_success'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
