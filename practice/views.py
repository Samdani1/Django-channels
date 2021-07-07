from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import Http404,HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your views here.
def index(request):
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        'GET_Data' , {
            'type' : 'send.message',
            'value': json.dumps({"test":"check"})
        }
    )
    return render(request, 'index.html')

def send_data(request, data):
    print(data)
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        'GET_Data' , {
            'type' : 'send.message',
            'value': json.dumps({"test":"check"})
        }
    )
    return JsonResponse({})

def rdata(request):
    if request.is_ajax and request.method == "GET":
        data = request.GET.get("nick_name", None)
        channel = get_channel_layer()
        async_to_sync(channel.group_send)(
            'GET_Data' , {
                'type' : 'send.message',
                'value': json.dumps({"dt":data})
            }
        )
    else:
        data = request.GET.get("nick_name", None)
        channel = get_channel_layer()
        async_to_sync(channel.group_send)(
            'GET_Data' , {
                'type' : 'send.message',
                'value': json.dumps({"dt":data})
            }
        )

    return HttpResponse( json.dumps([{'dt':'ok (request)'}]) )
    
