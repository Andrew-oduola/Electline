from django.urls import path
from . import views

app_name = 'elections'

urlpatterns = [
    path('voting/', views.voting_view, name='voting'),

]