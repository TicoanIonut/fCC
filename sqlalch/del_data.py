# deleting_data.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Artist).filter(Artist.name == "MXPX").first()
print(res.name)
session.delete(res)
session.commit()
print(res.name)

