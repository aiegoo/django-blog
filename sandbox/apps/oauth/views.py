from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from django.contrib import messages
# Create your views here.

@login_required
def profile_view(request):
    return render(request, 'oauth/profile.html')

@login_required
def change_profile_view (request):
    if request.method =='POST':
        # Uploading files requires request.FILES
        form = ProfileForm (request.POST, request.FILES, instance = request.user)
        if form.is_valid ():
            form.save ()
            # Add a message, the form is redirected to the personal information page
            messages.add_message (request, messages.SUCCESS, 'Personal information updated successfully!')
            return redirect ('oauth:profile')
    else:
        # Return empty form instead of POST request
        form = ProfileForm (instance = request.user)
    return render (request, 'oauth/change_profile.html', context = {'form': form})