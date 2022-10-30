import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

lista_link = []
numele_listei = 'Diverse.csv'
for x in range(1, 3):
	r = requests.get(f'https://www.pieseauto.ro/aprindere/?page={x}&utilizator=autolux')
	soup = BeautifulSoup(r.content, 'lxml')
	listaprodus = soup.find_all('a', class_='js-project-url')
	for link in listaprodus:
		lista_link.append(link['href'])


detalii = []
for link in lista_link:
	r = requests.get(link, headers=headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	titlu = soup.find('h1', itemprop="name").text        # titlu
	pret = soup.find('span', class_="price-item").text       # pret
	descriere = soup.find('div', itemprop="description").text.strip()      # descriere
	produse = titlu, pret, descriere
	detalii.append(produse)

	imagine = soup.select('img[src]')         # imagine
	image = imagine[2].get('src')
	if not image:
		image = None
	try:
		name = imagine[2].get('alt')
		filename = f'{numele_listei} {name}.jpg'
		res = requests.get(image)
		with open(filename.format(image), 'wb') as f:
			f.write(res.content)
	except:
		image = None


df1 = pd.DataFrame(lista_link)
df2 = pd.DataFrame(detalii)
df3 = pd.concat((df1, df2), axis=1)
df3 = pd.DataFrame(df3.values, columns=["Link", "Titlu", "Pret", "Descriere"])
df3.to_csv(f'{numele_listei}', index=False)
print(df3)
