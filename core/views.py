from django.shortcuts import redirect

# Create your views here.

def redirect_to_profile(request):
    return redirect('profile')
