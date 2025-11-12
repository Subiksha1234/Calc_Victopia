from django.shortcuts import render
from .models import Destination

def index(request):
 
    destinations = Destination.objects.all()

    for dest in destinations:
        if dest.offer:
            dest.desc += " (Special Offer!)"

    return render(request, 'travello/index.html', {'destinations': destinations})
