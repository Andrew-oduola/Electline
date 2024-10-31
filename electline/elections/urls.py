from django.urls import path
from . import views

app_name = 'elections'

urlpatterns = [
    path('', views.elections_view, name='elections'),
    path('vote/<slug:slug>/', views.vote_view, name='vote'),
]