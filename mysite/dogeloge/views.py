from django.shortcuts import render
from .models import DogWalker
from .models import DogOwner

def index(request):
        """Display Homepage Content"""
        dogwalkers = DogWalker.objects.all()
        dogowners = DogOwner.objects.all()
        return render(request, 'index.html', {'dogwalkers': dogwalkers})

