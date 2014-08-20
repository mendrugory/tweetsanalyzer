from django.shortcuts import render_to_response
from models import TweetSource
# Create your views here.

def source_research(request, sources=25):
    max_source = int(sources)
    tweet_sources = TweetSource.objects()[:max_source]
    return render_to_response("source_research.html", {"tweet_sources": tweet_sources})

