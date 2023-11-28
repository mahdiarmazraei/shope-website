from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://bingx.com/en-us/CopyTrading/1173556654743941121/?apiIdentity=1194211014359031809&rankStatisticDays=30&list_id=popular&from=1&accountEnum=BINANCE_FEATURE')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('div', class_="tavle-wrapper light")
    x = movies.find('table')
    y = x.find('tbody')
    z = y.find('tr')

    print(len(z))

except Exception as e:
    print(e)
    