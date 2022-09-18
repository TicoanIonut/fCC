import pandas as pd

df = pd.read_excel('Baza de date angajati.xlsx')
df.Salariu = pd.to_numeric(df.Salariu)
df = df.sort_values(by='Nume')
print(df['Nume'])
# df = df.sort_values(by='Salariu')
# df = df[df.Salariu > 2500]
# print(df)
filt = df['Nume'].str.startswith('Vla')
df = df.loc[filt]
print(df[['Nume', 'Salariu']])

