from django.shortcuts import render
from .models import Election

# Create your views here.

def elections_view(request):
    allowed_elections = [election for election in Election.objects.all() if election.is_voter_allowed(request.user.matric_no)]

    context = {
        'elections': allowed_elections,
        'voter': request.user,
    }
    return render(request, 'elections\\elections.html', context)


def vote_view(request, slug):
    
    election = Election.objects.get(slug=slug)
    candidates = election.candidates.all()
    context = {
        'election': election,
        'voter': request.user,
        'candidates': candidates,
    }
    return render(request, 'elections\\voting.html', context)

