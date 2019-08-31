from django.template import loader
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm


def index(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    latest_message_list = Message.objects.order_by('-pub_date')[:5]
    template = loader.get_template('chatting/index.html')
    context = {
        'form': form,
        'latest_message_list': latest_message_list,
    }
    return HttpResponse(template.render(context, request))


