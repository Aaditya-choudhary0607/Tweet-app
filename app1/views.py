from django.shortcuts import render
from .models import Tweet
from .forms import tweetform
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')


def tweetlist(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweetlist.html',{'tweets':tweets})

def tweetcreate(request):
    if request.method == "POST":
        form = tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetlist')
    else:
        form = tweetform()
    return render(request,'tweetfrom.html',{'form':form})




def tweetedit(request, tweetid):
    tweet=get_object_or_404(tweet, pk=tweetid,user = request.user)
    if request.method == "POST":
        form = tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetlist')
    else:
        form = tweetform(instance=tweet)
        return render(request,'tweetfrom.html',{'form':form})


def tweetdelete(request, tweetid):
    tweet = get_object_or_404(Tweet, pk=tweetid, user = request.user)
    if request.method == "POST":
        Tweet.delete()
        return redirect('tweetlist')
    return render(request, 'tweet_confirm_delete.html',{'tweet':tweet})    
