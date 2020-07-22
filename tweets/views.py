import random
from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html", context={}, status=200)
    #print(args,kwargs)
    #return HttpResponse("<h1>Hello World</h1>")
"""
Restful api view
returns json data
so we can consume via js, swift, java, iOS/android

"""

def tweet_detail_view(request, tweet_id,*args, **kwargs):
    data={
        "id": tweet_id,
        #"image_path":obj.image.url  
         }
    status = 200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
#HttpResponse(f"<h1>Hello {tweet_id}-{obj.content}</h1>")


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all() #qs=queryset, a convention
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,121)} for x in qs] #iterating through the list 
    data = {
        "response":tweets_list
        }
    return JsonResponse(data)
