__author__ = 'mendrugory'

import multiprocessing
from tweetsanalyzer.twitter_processing.models import Tweet
from tweetsanalyzer.source_research.models import TweetSource


class TweetProcessor(object):
    '''
    Base class in order to process a tweet
    '''

    def __init__(self, model):
        self.document = None
        self.model = model

    def run(self, tweet):
        '''
        The function which will be launch in the process
        '''
        self.process(tweet)
        self.save()


    def process(self, tweet):
        '''
        Main method of the class. It will have to be implemented by the child classes.
        '''
        filter_key = self.get_the_key(tweet)
        self.document = self.get_the_document(filter_key)

    def get_the_document(self, filter_key):
        '''
        Retrieve the document
        '''
        query = self.model.objects(filter_key=filter_key).limit(1)
        if len(query) == 0:
            document = self.model()
        else:
            document = query[0]
        return document

    def save(self):
        '''
        Save into database the document.
        '''
        self.document.save()

    def get_the_key(self, tweet):
        '''
        Obtain the key from the tweet which will be used as filter
        '''
        pass

    def update_value(self):
        '''
        Update method for the main value
        '''
        pass


class SourceProcessor(TweetProcessor):
    '''
    Class to process the source of the tweet
    '''

    def __init__(self, tweet_source):
        super(SourceProcessor, self).__init__(tweet_source)

    def process(self, tweet):
        super(SourceProcessor, self).process(tweet)
        if self.document.filter_key is None:
            self.document.filter_key = self.get_the_source(tweet.source)
            self.document.source = tweet.source
        self.document.last_change = tweet.created_at
        self.document.count += 1
        self.update_value()

    def get_the_key(self, tweet):
        '''
        Get the key
        '''
        source = tweet.source
        return self.get_the_source(source)

    def get_the_source(self, source):
        '''
        Get the source from the tweet
        '''
        key = source.split(">")[1].split("<")[0].strip()
        return key.encode("utf-8")

    def update_value(self):
        '''
        Update method for the main value
        '''
        self.document.value += 1

