from django.shortcuts import render
import urllib
import json



def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        api_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=a986e972e2d8bea4cae79f86fdc7c21b').read()
        api_url2 = json.loads(api_url)


        data = {
            'city':city,
            'weather':api_url2['weather'][0]['description'],
            'temperature':api_url2['main']['temp'],
            'temp_min':api_url2['main']['temp_min'],
            'temp_max':api_url2['main']['temp_max'],
            'pressure':api_url2['main']['pressure'],
            'humidity':api_url2['main']['humidity'],
            'country':api_url2['sys']['country']
        }

    else:
        data = {
            'city':None,
            'weather':None,
            'temperature':None,
            'temp_min':None,
            'temp_max':None,
            'pressure':None,
            'humidity':None,
            'country':None
        } 

    return render(request, "HTML/index.html",{'data':data})