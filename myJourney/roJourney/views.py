from django.shortcuts import render
from .models import Profile, LearningEntry

def index(request):
    """Home page showing learning journey entries."""
    entries = LearningEntry.objects.order_by('-date')
    context = {'entries': entries}
    return render(request, 'roJourney/index.html', context)

def about_me(request):
    """About page showing all profiles."""
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'roJourney/aboutMe.html', context)

