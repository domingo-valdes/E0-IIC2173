import requests
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Message
from .forms import MessageForm


def index(request):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?q=santiago,cl&APPID=8a714970fbc38e21879bb1a4a1e986e9'
    json_data = requests.get(api_address).json()
    weather_description = json_data['weather'][0]['description']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    temperature = str(int(json_data['main']['temp']) - 273)

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    # latest_message_list = Message.objects.order_by('-pub_date')[:5]
    latest_message_list = Message.objects.order_by('-id')[:100]
    page = request.GET.get('page',1)
    paginator = Paginator(latest_message_list, 5)
    template = loader.get_template('chatting/index.html')
    context = {
        'form': form,
        'messages': paginator.page(page),
        'weather_description': weather_description,
        'pressure': pressure,
        'humidity': humidity,
        'temperature': temperature
    }
    return render(request, 'chatting/index.html', context)
    #return HttpResponse(template.render(context, request))




