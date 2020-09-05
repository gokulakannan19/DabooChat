from django.shortcuts import render
from .models import Profile
# Create your views here.


def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)

    context = {
        'obj': obj
    }

    return render(request, 'profiles/my_profile.html', context)
