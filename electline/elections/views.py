# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, Election, Vote

def elections_view(request):
    allowed_elections = [election for election in Election.objects.all() if election.is_voter_allowed(request.user.matric_no)]
    context = {
        'elections': allowed_elections,
        'voter': request.user,
    }
    return render(request, 'elections\\elections.html', context)

def vote_view(request, slug):
    election = get_object_or_404(Election, slug=slug)
    candidates = election.candidates.all()

    button_state =''
    if Vote.objects.filter(user=request.user, election=election).exists():
        button_state = 'disabled'

    context = {
        'election': election,
        'voter': request.user,
        'candidates': candidates,
        'button_state': button_state,
    }
    return render(request, 'elections\\voting.html', context)

def cast_vote(request, slug, candidate_id):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, pk=candidate_id)
        election = get_object_or_404(Election, slug=slug)

        # Ensure the voter hasn't voted in this election already
        if Vote.objects.filter(user=request.user, election=election).exists():
            # Optionally, you could redirect with a message saying the user has already voted
            return redirect(election.get_absolute_url())

        vote = Vote.objects.create(user=request.user, candidate=candidate, election=election)
        vote.save()
        return redirect(election.get_absolute_url())
