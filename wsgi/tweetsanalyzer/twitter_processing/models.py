__author__ = 'mendrugory'

import mongoengine


class Tweet(mongoengine.Document):
    created_at = mongoengine.StringField(max_length=200)
    tweet_id = mongoengine.IntField(default=-1)
    tweet_text = mongoengine.StringField(max_length=500)
    source = mongoengine.StringField(max_length=200)
    retweet_count = mongoengine.IntField(default=0)
    favorite_count = mongoengine.IntField(default=0)
    lang = mongoengine.StringField(max_length=5)
    #user = User()
    favorited = mongoengine.BooleanField(default=False)
    retweeted = mongoengine.BooleanField(default=False)
    filter_level = mongoengine.StringField(max_length=60)
    latitude = mongoengine.FloatField(default=None)
    longitude = mongoengine.FloatField(default=None)

    def __repr__(self):
        return str(Tweet.source.to_python('utf-8'))

class User(mongoengine.EmbeddedDocument):
    user_id = mongoengine.IntField(default=-1)
    name = mongoengine.StringField(max_length=200)
    screen_name = mongoengine.StringField(max_length=200)
    location = mongoengine.StringField(max_length=200)
    description = mongoengine.StringField(max_length=200)
    followers_count = mongoengine.IntField(default=0)
    friends_count = mongoengine.IntField(default=0)
    geo_enabled = mongoengine.BooleanField(default=False)
    lang = mongoengine.StringField(max_length=5)
    created_at = mongoengine.StringField(max_length=200)
    bck_image_url = mongoengine.StringField(max_length=200)
    profile_image_url = mongoengine.StringField(max_length=200)

