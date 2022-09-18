from peewee import *

database = SqliteDatabase('db.sqlite')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Artists(BaseModel):
    artist = TextField(null=True)
    reviewid = IntegerField(null=True)

    class Meta:
        table_name = 'artists'
        primary_key = False

class Content(BaseModel):
    content = TextField(null=True)
    reviewid = IntegerField(null=True)

    class Meta:
        table_name = 'content'
        primary_key = False

class Genres(BaseModel):
    genre = TextField(null=True)
    reviewid = IntegerField(null=True)

    class Meta:
        table_name = 'genres'
        primary_key = False

class Labels(BaseModel):
    label = TextField(null=True)
    reviewid = IntegerField(null=True)

    class Meta:
        table_name = 'labels'
        primary_key = False

class Reviews(BaseModel):
    artist = TextField(null=True)
    author = TextField(null=True)
    author_type = TextField(null=True)
    best_new_music = IntegerField(null=True)
    pub_date = TextField(null=True)
    pub_day = IntegerField(null=True)
    pub_month = IntegerField(null=True)
    pub_weekday = IntegerField(null=True)
    pub_year = IntegerField(null=True)
    reviewid = IntegerField(null=True)
    score = FloatField(null=True)
    title = TextField(null=True)
    url = TextField(null=True)

    class Meta:
        table_name = 'reviews'
        primary_key = False

class Years(BaseModel):
    reviewid = IntegerField(null=True)
    year = IntegerField(null=True)

    class Meta:
        table_name = 'years'
        primary_key = False

