from database_models_sqalch import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# res = session.query(Player).filter(Player.height > 195)
# for s in res:
# 	print(s.player_name)

res = session.query(Player).order_by(Player.height)
for s in res:
	print(s.player_name)

