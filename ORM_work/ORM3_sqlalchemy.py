from database_models_sqalch import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

i = 0
res = session.query(Player).filter(Player.height > 195).filter(Player.weight > 200).order_by(Player.player_name)
for s in res:
	r = i, s.player_name, s.height, s.weight
	print(r)
	i += 1

