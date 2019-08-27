from django.shortcuts import render
from .models import Message



def index(request):
    latest_message_list = Message.objects.order_by('-pub_date')[:5]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'chatting/index.html', context)
