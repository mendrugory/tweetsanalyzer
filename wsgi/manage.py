#!/usr/bin/env python
import os
import sys
import mongoengine
from multiprocessing import Process
from tweetsanalyzer.settings import MONGODB_HOST
from tweetsanalyzer.settings import MONGODB_NAME
from tweetsanalyzer import twitter_streaming

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweetsanalyzer.settings")

    mongodb_connection = mongoengine.connect(MONGODB_NAME, host=MONGODB_HOST)
    process = Process(target=twitter_streaming)
    process.start()
    print "Process in order to collect tweets started."

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
