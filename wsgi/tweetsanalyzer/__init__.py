__author__ = 'mendrugory'


from twitter_processing.twitter_communication import TwitterStreaming

MY_TECH_LIST = ["python", "big data", "smart cities", "nosql", "datascience", "datascientist", \
                "IoT", "M2M", "django", "flask", "numpy", "scipy", "RPi", "raspberry pi", "arduino",\
                "sql", "android", "cloud", "mobile", "linux", "ubuntu"]

MY_BIG_DATA_LIST = ["big data", "big_data", "bigdata", "big-data"]

MY_LIST = MY_BIG_DATA_LIST + [word.upper() for word in MY_BIG_DATA_LIST]


def twitter_streaming():
    twitter_stream = TwitterStreaming()
    twitter_stream.run(tracking=MY_LIST)
