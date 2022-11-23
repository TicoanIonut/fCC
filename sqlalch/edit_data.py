from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# # querying for a record in the Artist table
# res = session.query(Artist).filter(Artist.name == "Kutless").first()
# print(res.name)
#
# # changing the name
# res.name = "Beach Boys"
# session.commit()
# print(res.name)


# how to do a JOINed query
# editing Album data
artist, album = session.query(Artist, Album).filter(Artist.id == Album.artist_id).filter(Album.title == "Thrive").first()
print(album.title)
album.title = "Step Up to the Microphone"
session.commit()
print(album.title)


# session.rollback()          #for rollback
