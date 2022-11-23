import peewee

db = peewee.SqliteDatabase('piui.db')


class Artist(peewee.Model):
	name = peewee.CharField()
	
	class Meta:
		database = db


class Album(peewee.Model):
	artist = peewee.ForeignKeyField(Artist)
	title = peewee.CharField()
	release_date = peewee.DateTimeField()
	publisher = peewee.CharField()
	media_type = peewee.CharField()
	
	class Meta:
		database = db


if __name__ == "__main__":
	try:
		Artist.create_table()
	except peewee.OperationalError:
		print("Artist table already exists!")
	
	try:
		Album.create_table()
	except peewee.OperationalError:
		print("Album table already exists!")