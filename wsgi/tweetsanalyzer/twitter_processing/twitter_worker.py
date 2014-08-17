__author__ = 'mendrugory'

import multiprocessing
from tweetsanalyzer.twitter_processing.tweet_process import TweetProcessor


class Worker(multiprocessing.Process):
    '''
    The class which will generate an independant process in order to process the tweet for
    a particular study.
    '''

    def __init__(self, tweet_processor, tweet):
        '''
        Child class of processor. It needs a TweetProcessor class in order to be launch in a new process.
        '''
        super(Worker, self).__init__(target=tweet_processor.run, args=(tweet,))
