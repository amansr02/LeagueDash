from django.urls import path
from . import views

urlpatterns = [
    path('teams/',views.teams,name='teams'),
    path('matches/',views.match,name='matches'),
    path('<slug:team_id>/team',views.team_detail,name='team'),
]