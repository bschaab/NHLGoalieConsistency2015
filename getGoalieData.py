#from lxml import html
#import requests

#page = requests.get('http://www.hockey-reference.com/leagues/NHL_2015_goalies.html')
#tree = html.fromstring(page.content)

#for i in range (1,101):
#	temp = tree.xpath('//*[@id="stats"]/tbody/tr[i]/td[2]/href/text()')
#	print temp

from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "http://www.hockey-reference.com/leagues/NHL_2015_goalies.html"

html = urlopen(url)

soup = BeautifulSoup(html)


data_rows = soup.findAll('tr')[2:] 

player_names = []
overall_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]

for row in overall_data:
	if row:
		player_names.append(row[1].encode('ascii','ignore'))

print player_names

