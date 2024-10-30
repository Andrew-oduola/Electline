from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import MatricNoLoginForm

# Create your views here.
def login_view(request):
    form = MatricNoLoginForm()
    if request.method == 'POST':
        form = MatricNoLoginForm(request.POST)
        if form.is_valid():
            matric_no = form.cleaned_data['matric_no']
            password = form.cleaned_data['password']
            user = authenticate(matric_no=matric_no, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the voting page
                return redirect('elections:voting')
            else:
                print('incorrect user')
        else:
            print('invalid form')
            print(form.errors)
    return render(request, 'accounts/login.html', {'form': form})   


