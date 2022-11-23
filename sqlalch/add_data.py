import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
new_artist = Artist("Newsboys")
new_artist.albums = [Album("Read All About It",
                           datetime.date(1988, 12, 1),
                           "Refuge", "CD")]

# add more albums
more_albums = [Album("Hell Is for Wimps",
                     datetime.date(1990, 7, 31),
                     "Star Song", "CD"),
               Album("Love Liberty Disco",
                     datetime.date(1999, 11, 16),
                     "Sparrow", "CD"),
               Album("Thrive",
                     datetime.date(2002, 3, 26),
                     "Sparrow", "CD")]
new_artist.albums.extend(more_albums)

# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()

# Add several artists
session.add_all([
    Artist("MXPX"),
    Artist("Kutless"),
    Artist("Thousand Foot Krutch")
    ])
session.commit()
