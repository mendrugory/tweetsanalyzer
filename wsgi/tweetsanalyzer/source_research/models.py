import mongoengine


class TweetSource(mongoengine.Document):
    source = mongoengine.StringField(max_length=200, default=None)
    filter_key = mongoengine.StringField(max_length=200, default=None)
    count = mongoengine.IntField(default=0)
    last_change = mongoengine.StringField()
    value = mongoengine.IntField(default=0)
    url = mongoengine.StringField(max_length=200, default="http://www.twitter.com")

    meta = {
        'indexes': ['filter_key', ('filter_key', '-value')],
        'ordering': ['-value']
    }

