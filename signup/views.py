import signup
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm

# Create your views here.
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # create new user
            
            username = form.cleaned_data['username']
            password_actual = form.cleaned_data['password1']

            user = authenticate(username=username, password=password_actual)
            if user is not None:
                login(request, user)
                return redirect('profile')
            
            return redirect('signup')  # this will redirect user to the same page (if registration fails)

    else:
        form = SignUpForm()


    return render(request, 'signup/register.html', {'form':form})