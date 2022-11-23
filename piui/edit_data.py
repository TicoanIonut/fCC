from models import Album, Artist

import peewee
# band = Artist.select().where(Artist.name == "Kutless").get()
# print(band.name)

# shortcut method
# band = Artist.get(Artist.name == "Kutless")
# print(band.name)
# #
# #
# # change band name
# band.name = "Beach Boys"
# band.save()
# print(band.name)
#
album = Album.select().join(Artist).where(
    (Album.title == "Thrive") & (Artist.name == "Newsboys")
    ).get()
album.title = "Step Up to the Microphone"
album.save()
print(album.title)
#
#
# query = Album.select().join(Artist)
# qry_filter = (Album.title == "Step Up to the Microphone") & (Artist.name == "Newsboys")
# album = query.where(qry_filter).get()
# print(album.artist.name)
