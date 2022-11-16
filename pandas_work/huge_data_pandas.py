import pandas as pd



mr = pd.Series([], dtype='float64')


df = pd.read_csv('datadog.csv', nrows=100, skiprows=100)
df.columns = ['a', 'c', 'd', 'e']
# mr = pd.concat([mr, df.a / df.k])
# print(df)


counter = 0
for chunk in pd.read_csv('datadog.csv', chunksize=10):
	chunk.columns = ['a', 'c', 'd', 'e']
	# mr = pd.concat([mr, chunk.a / chunk.k])
	counter += 1
	if counter == 25:
		break
print(chunk)