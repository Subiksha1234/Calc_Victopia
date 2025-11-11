from django.shortcuts import render

def index(request):
    destinations = [
        {'name': 'Bali', 'price': 500},
        {'name': 'Paris', 'price': 700},
        {'name': 'Maldives', 'price': 900},
        {'name': 'Tokyo', 'price': 800},
        {'name': 'Rome', 'price': 650},
        {'name': 'London', 'price': 750},
        {'name': 'New York', 'price': 850},
        {'name': 'Sydney', 'price': 950},
        {'name': 'Cape Town', 'price': 600},
        {'name': 'Barcelona', 'price': 700},
        {'name': 'Venice', 'price': 720},
        {'name': 'Bangkok', 'price': 550},
        {'name': 'Dubai', 'price': 800},
        {'name': 'Egypt', 'price': 500},
        {'name': 'Mauritius', 'price': 900},
    ]
    return render(request, 'travello/index.html', {'destinations': destinations})

