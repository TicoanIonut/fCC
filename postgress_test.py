import psycopg2
from utils import POSTGRES_PAS


conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password=POSTGRES_PAS, port=5432)
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS person (
# id INT PRIMARY KEY,
# name VARCHAR(255),
# age INT,
# gender CHAR
# )
# """);
#
#
# cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
# (1, 'Mike1', 31, 'm'),
# (2, 'Mike2', 32, 'm'),
# (3, 'Mike3', 33, 'm'),
# (4, 'Mike4', 34, 'm'),
# (5, 'Mike5', 35, 'm');
# """);

cur.execute("""SELECT * FROM person WHERE name = 'Mike3'; """)
print(cur.fetchone(), 'one')
cur.execute("""SELECT * FROM person WHERE age < 34; """)
# print(cur.fetchall())
for row in cur.fetchall():
	print(row)
sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age > %s;""", ("M", 32))
print(sql)
cur.execute(sql)
for row in cur.fetchall():
	print(row)

conn.commit()
cur.close()
conn.close()
