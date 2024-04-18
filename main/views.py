
from django.shortcuts import render
from main.models import Location
import requests

def index(request):
    locations = Location.objects.all()
    return render(request, 'main/index.html', {'locations': locations})

def fetch_data(request, postcode):
    locations = Location.objects.all()
    url = f'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}'
    r = requests.get(url, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15' })
    if r.status_code == 200:
        postcode_city = Location.objects.get(postcode=postcode)
        display = format_data(r.json())
        return render(request, 'main/index.html', {'locations': locations,
                                                   'display': display,
                                                   'postcode_city': postcode_city
                                                   })
    else:
        print(f'Cannot fetch data, {r.status_code}')


def format_data(data):
    restaurant_data = data['restaurants']
    lookup = {}
    for i in range(10):
        lookup[restaurant_data[i]['name']]={
                   'rating': restaurant_data[i]['rating']['count'],
                   'cuisines': restaurant_data[i]['cuisines'],
                   'address': restaurant_data[i]['address']}
    return lookup











