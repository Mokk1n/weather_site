from requests import get
from django.shortcuts import render
from .forms import CityForm
from .models import City


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=0fbf3c3afac48c7bf1d1491776e2cf32'
        res1 = get(weather_api).json()
        try:
            city_info = {
                'city': city.name,
                'temp': res1["main"]["temp"],
                'icon': res1["weather"][0]["icon"],
            }
            all_cities.append(city_info)
        except:
            continue
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
