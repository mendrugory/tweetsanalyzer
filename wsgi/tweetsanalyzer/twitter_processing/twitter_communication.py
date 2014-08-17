__author__ = 'mendrugory'

import sys
import json
import tweepy

import tweetsanalyzer.settings as secret
from tweetsanalyzer.twitter_processing.models import Tweet
from tweetsanalyzer.twitter_processing.tweet_process import SourceProcessor
from tweetsanalyzer.source_research.models import TweetSource
from tweetsanalyzer.twitter_processing.twitter_worker import Worker


class CustomStreamListener(tweepy.StreamListener):
    '''
    Custom class to manage the twitter streaming
    '''

    def __init__(self):
        super(CustomStreamListener, self).__init__()


    def on_data(self, tweet):
        pass

    def on_status(self, status):
        '''
        Get the streaming status
        '''
        print status.text

    def on_error(self, status_code):
        '''
        don't kill the stream although an error happened.
        '''
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        '''
        don't kill the stream although a timeout happened.
        '''
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


class MongoDBStreamListener(CustomStreamListener):

    def __init__(self):
        super(MongoDBStreamListener, self).__init__()

    def on_data(self, tweet):
        super(MongoDBStreamListener, self).on_data(tweet)
        json_tweet = json.loads(tweet)
        doc = self.process_tweet(json_tweet)
        self.process_all_studies(doc)

    def on_status(self, status):
        super(MongoDBStreamListener, self).on_status(status)

    def on_error(self, status_code):
        '''
        don't kill the stream although an error happened.
        '''
        super(MongoDBStreamListener, self).on_error(status_code)

    def on_timeout(self):
        super(MongoDBStreamListener, self).on_timeout()

    def process_tweet(self, tweet):
        doc = Tweet()
        doc.created_at = tweet["created_at"]
        doc.favorite_count = tweet["favorite_count"]
        doc.favorited = tweet["favorited"]
        doc.lang = tweet["lang"]
        doc.retweet_count = tweet["retweet_count"]
        doc.retweeted = tweet["retweeted"]
        doc.source = tweet["source"]
        doc.tweet_text = tweet["text"]
        doc.filter_level = tweet["filter_level"]
        doc.tweet_id = tweet["id"]
        if tweet["coordinates"] is not None:
            doc.longitude = tweet["coordinates"]["coordinates"][0]
            doc.latitude = tweet["coordinates"]["coordinates"][1]
        doc.save()
        return doc

    def process_all_studies(self, tweet):
        source_worker = Worker(SourceProcessor(TweetSource), tweet)
        source_worker.start()


    def get_user_info(self, tweet):
        pass


class TwitterAuth(object):
    '''
    class to manage the twitter authorization
    '''

    def __init__(self):
        self.auth = tweepy.OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
        self.auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def get_auth(self):
        return self.auth

    def get_api(self):
        return self.api


class TwitterStreaming(object):
    '''
    Twitter Streaming
    '''

    def __init__(self, stream_listener=MongoDBStreamListener, auth=TwitterAuth):
        self.twitter_auth = auth()
        self.stream_listener = stream_listener


    def run(self, tracking=None, locations=None):
        '''
        Run the streaming

        tracking: list of topics
        '''

        sapi = tweepy.streaming.Stream(self.twitter_auth.get_auth(), self.stream_listener())
        sapi.filter(track=tracking, locations=[])
