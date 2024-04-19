
from django.shortcuts import render
from main.models import Location
import requests

# Renders and returns  the index page and passes the 'location' objects as context
# to populate the droplist containing postcodes and their respective areas
def index(request):
    locations = Location.objects.all()
    return render(request, 'main/index.html', {'locations': locations})

# Using Django's rendering, it passes the postcode from the selected object in the droplist
# Inside the function, the API url is pre-stored where {postcode} is the postcode that was passed as a parameter
def fetch_data(request, postcode):
    locations = Location.objects.all()

    # Pre-stored URL
    url = f'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}'

    # Making a request using Python's request library and adding some headers for security
    r = requests.get(url, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15' })

    # Execute the logic if the call is successful
    if r.status_code == 200:

        # Used to display the name of the selected postcode and its respective area
        postcode_area = Location.objects.get(postcode=postcode)

        # function format_data() returns formatted data focused on 'restaurants' in a form of dictionary
        # Assigns dictionary of keys and values to 'display' variable that will be passed on to the HTML to display data
        display = format_data(r.json())
        return render(request, 'main/index.html', {'locations': locations,
                                                   'display': display,
                                                   'postcode_area': postcode_area
                                                   })
    # Raise an error otherwise
    else:
        print(f'Cannot fetch data, {r.status_code}')


def format_data(data):
    # Filter the json body to the 'restaurants' key
    restaurant_data = data['restaurants']

    # Initialize a variable to store the data
    lookup = {}

    # Loops through the first 10 restaurants and creates key-value pairs for data access
    for i in range(10):
        lookup[restaurant_data[i]['name']] = {
                   'rating': restaurant_data[i]['rating']['count'],
                   'cuisines': restaurant_data[i]['cuisines'],
                   'address': restaurant_data[i]['address']}
    return lookup











