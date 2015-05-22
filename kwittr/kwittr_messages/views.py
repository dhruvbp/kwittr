from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from kwittr_messages.models import Message

def message_listing(request):

    if request.method == 'POST':
        new_message = request.POST.get('new_message')
        if new_message:
            message = Message()
            message.message = new_message
            message.created_datetime = timezone.now()
            message.created_by = request.user
            message.save()

    messages = Message.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(messages, 5)
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    context = {
        'messages': messages,
        }
    return render(request, 'kwittr_messages/message_listing.html', context)


def message_details(request, post_id):
    message = Message.objects.get(pk=post_id)
    context = {'message': message}
    return render(request, 'kwittr_messages/message_details.html', context)    


@login_required
def message_add_likes(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.likes = message.likes + 1
    message.save()
    data = {'likes_updated': message.likes}
    return JsonResponse(data)
   



