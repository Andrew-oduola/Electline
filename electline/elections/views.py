from django.shortcuts import render

# Create your views here.
def voting_view(request):
    
    context = {
        'voter': request.user,
    }
    return render(request, 'elections\\voting.html', context)