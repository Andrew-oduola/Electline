from django.shortcuts import render

from .forms import MatricNoLoginForm

# Create your views here.
def login_view(request):
    form = MatricNoLoginForm()
    return render(request, 'accounts/login.html', {'form': form})   


def voting_view(request):
    return render(request, 'accounts/voting.html')