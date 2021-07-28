from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import yahoo_fin.stock_info as si
import csv

now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")

with open('aad_data.csv') as file:
    if date in file.read():
        pass
    else:
        html = urlopen('https://www.amadeus-fire.de/jobs-und-karriere/stellenangebote/')
        bs = BeautifulSoup(html.read(), 'html.parser')
        st = bs.find('span', {'class':"jsr-count f-primary-sb"})
        st = st.get_text()
        st = int(float(st)*1000)

        mcap = si.get_quote_table('AAD.DE')['Market Cap']
        mcap = int(float(mcap[:-1])*1000000)

        data = date, st, mcap
        with open('aad_data.csv', "a", encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow([date, st, mcap])
