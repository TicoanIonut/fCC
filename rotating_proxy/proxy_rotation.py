import requests

with open('valid_proxy.txt', 'r') as f:
	proxies = f.read().split('\n')
# print(len(proxies))

sites_to_check = ['http://books.toscrape.com/',
                  'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
                  'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
                  ]
counter = 0

for site in sites_to_check:
	try:
		print(f'using the proxy: {proxies[counter]}')
		res = requests.get(site, proxies={'http': proxies[counter],
		                                  'https:': proxies[counter]})
		print(res.status_code)
	except:
		print('fail')
	finally:
		counter += 1
		counter % len(proxies)
