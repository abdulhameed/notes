from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from notes.models import UserProfile
from notes.user_profiles import regular_context


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            UserProfile.objects.create(user=new_user)
            authed_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authed_user)
            return redirect('home')

    # Render
    context = regular_context(request.user)
    context['form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            data = form.clean()
            authed_user = authenticate(username=data['username'], password=data['password'])

            # Create user profile if one does not exist (for users made through createsuperuser)
            if not UserProfile.objects.filter(user=authed_user).exists():
                UserProfile.objects.create(user=authed_user)

            login(request, authed_user)
            return redirect('home')

    # Render
    context = regular_context(request.user)
    context['form'] = form
    return render(request, 'login.html', context)
