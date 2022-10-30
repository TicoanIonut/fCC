import pandas as pd
from db_models_pwi import *


# con = Reviews.select(Reviews.artist).filter(Reviews.score < 6)
qry = Reviews.select(Reviews).filter(Reviews.score < 6)
# print(qry)
# print(con)

# rrr = []
#
# for s in con:
# 	s.artist = '111' + s.artist
# 	rrr.append({'artist': s.artist})
# 	# print(s.artist)
# df1 = pd.DataFrame(rrr)
# print(df1.describe())


lll = []
for i in qry:
	i.artist = '111' + i.artist
	lll.append({'artist': i.artist,
	            'title': i.title,
	            'reviewid': i.reviewid,
	            'score': i.score,
	            # 'url': i.url
	            })
df = pd.DataFrame(lll)
# print(df.describe)
print(df)
# rez = pd.concat([df1, df], axis=1)
# print(rez)
