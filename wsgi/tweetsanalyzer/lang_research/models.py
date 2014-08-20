import mongoengine


class TweetLanguage(mongoengine.Document):
    language = mongoengine.StringField(max_length=209, default=None)
    filter_key = mongoengine.StringField(max_length=209, default=None)
    count = mongoengine.IntField(default=0)
    last_change = mongoengine.StringField()
    value = mongoengine.IntField(default=0)

    meta = {
        'indexes': ['filter_key', ('filter_key', '-value')],
        'ordering': ['-value']
    }