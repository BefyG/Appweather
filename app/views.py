# weather/views.py
import requests
from django.shortcuts import render

# Replace this with your OpenWeatherMap API key
API_KEY = 'e219dfa588188b39a90ed710a0c9477a'

def weather_view(request):
    weather_data = None
    city = ''
    
    if request.method == "POST":
        # Get city from form
        city = request.POST.get('city')
        
        # Build the API URL
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        
        # Make the request
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Extract the needed info
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            # Handle invalid city or API error
            weather_data = {'error': 'City not found or API error'}
    
    # Pass weather data to template
    return render(request, 'weather/weather.html', {'weather': weather_data, 'city': city})
