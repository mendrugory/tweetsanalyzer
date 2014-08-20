#!/usr/bin/env python
import os
import sys
import time
import mongoengine
from multiprocessing import Process
from tweetsanalyzer.settings import MONGODB_HOST
from tweetsanalyzer.settings import MONGODB_PORT
from tweetsanalyzer.settings import MONGODB_NAME
from tweetsanalyzer.settings import MONGODB_USER
from tweetsanalyzer.settings import MONGODB_PWD
from tweetsanalyzer import twitter_streaming



def db_and_twitter_connection():
    try:
        if MONGODB_USER is None:
            mongodb_connection = mongoengine.connect(MONGODB_NAME, alias="default", host=MONGODB_HOST)
        else:
            mongodb_connection = mongoengine.connect(MONGODB_NAME, alias="default",\
                                                     host=MONGODB_HOST, port=MONGODB_PORT,\
                                                     username=MONGODB_USER, password=MONGODB_PWD)
        process = Process(target=twitter_streaming)
        process.start()
        time.sleep(5)

        if process.is_alive():
            print "Process in order to collect tweets started."
        else:
            print "The process is not alive"
    except Exception as ex:
        print "Error:", ex.message

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweetsanalyzer.settings")

    db_and_twitter_connection()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
