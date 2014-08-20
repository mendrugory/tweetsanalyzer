from django.shortcuts import render_to_response
from models import TweetSource
# Create your views here.

def source_research(request):
    tweet_sources = TweetSource.objects()[:25]
    return render_to_response("lang_research.html", {"tweet_sources": tweet_sources})

