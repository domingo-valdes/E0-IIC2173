from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Message
from .forms import MessageForm


def index(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    # latest_message_list = Message.objects.order_by('-pub_date')[:5]
    latest_message_list = Message.objects.order_by('-id')[:100][::-1]
    page = request.GET.get('page',1)
    paginator = Paginator(latest_message_list, 5)
    template = loader.get_template('chatting/index.html')
    context = {
        'form': form,
        'messages': paginator.page(page),
    }
    return render(request, 'chatting/index.html', context)
    #return HttpResponse(template.render(context, request))


# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'core/user_list.html', { 'users': users })


