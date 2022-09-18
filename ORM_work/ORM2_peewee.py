from db_models_pwi import *

reviews = Reviews.select().join(Genres).get()
print(reviews.artist)
