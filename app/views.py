
import requests
from django.shortcuts import render
from .models import WeatherRecord

API_KEY = 'e219dfa588188b39a90ed710a0c9477a'

def weather(request):
    weather_data = None
    city = ''
    
    icon_map = {
        "01d": "☀️", "01n": "🌙",
        "02d": "🌤️", "02n": "☁️",
        "03d": "☁️", "03n": "☁️",
        "09d": "🌧️", "09n": "🌧️",
        "10d": "🌦️", "10n": "🌦️",
        "11d": "⛈️", "11n": "⛈️",
        "13d": "❄️", "13n": "❄️",
        "50d": "🌫️", "50n": "🌫️",
    }
    
    if request.method == "POST":

        city = request.POST.get('city')
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
        
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        
            weather_data['emoji'] = icon_map.get(data['weather'][0]['icon'], "🌤️")
            
            # Save to database
            WeatherRecord.objects.create(
                city=weather_data['city'],
                temperature=weather_data['temperature'],
                description=weather_data['description'],
                icon=weather_data['icon'],
                emoji=weather_data['emoji']
            )
        else:
            
            weather_data = {'error': 'City not found or API error'}
    

    return render(request, 'weather/weather.html', {'weather': weather_data, 'city': city})

def weather_history(request):
    records = WeatherRecord.objects.all().order_by('-timestamp')
    return render(request, 'weather/history.html', {'records': records})

def about(request):
    return render(request, 'weather/about.html')