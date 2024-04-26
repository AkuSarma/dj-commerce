from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_store(request):
    context = {
        'user' : request.user,
    }
    return render(request, 'store/home-store.html', context)