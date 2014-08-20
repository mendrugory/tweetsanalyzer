from django.shortcuts import render_to_response
from models import TweetLanguage
# Create your views here.

def lang_research(request, langs=25):
    max_langs = int(langs)
    tweet_langs = TweetLanguage.objects()[:max_langs]
    return render_to_response("lang_research.html", {"tweet_langs": tweet_langs})