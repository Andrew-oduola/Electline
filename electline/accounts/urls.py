from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('voting/', views.voting_view, name='voting')
]