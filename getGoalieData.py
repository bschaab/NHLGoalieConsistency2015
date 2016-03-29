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
split_names = []
temp = []

overall_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]

for row in overall_data:
	if row:
		if (int(row[4]) >= 20):
			player_names.append(row[1].encode('ascii','ignore'))

#now have a list of goalies who played more than 20 games in 2015

firsturl = "http://www.hockey-reference.com/players/"
secondurl = "gamelog/2015/"

for player in player_names:
	print player.split()
		

