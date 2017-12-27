from lxml import html
import requests
import os
import csv

years = [2011, 2012, 2013, 2014, 2015, 2016]
positions = [['quarterback' , 'QB'],
			 ['wide-receiver', 'WR'],
			 ['tight-end', 'TE'],
			 ['fullback', 'FB'],
			 ['tackle', 'T'],
			 ['left-tackle', 'LT'],
			 ['right-tackle', 'RT'],
			 ['guard', 'G'],
			 ['center', 'C'],
			 ['defensive-line', 'DL'],
			 ['defensive-end', 'DE'],
			 ['defensive-tackle', 'DT'],
			 ['linebacker', 'LB'],
			 ['outside-linebacker', 'OLB'],
			 ['inside-linebacker', 'ILB'],
			 ['cornerback', 'CB'],
			 ['safety', 'S']]

for year in years:
	for position in positions:
		
		# Send request and get page source from requested site
		page = requests.get('http://www.spotrac.com/nfl/rankings/' + str(year) + '/average/' + position[0] + '/')
		tree = html.fromstring(page.content)

		# finds specific CSS headers that come before required information (player names, salaries in this case)
		players = tree.xpath('//a[@class="team-name"]/text()')
		salaries = tree.xpath('//span[@class="info"]/text()')

		numberSalaries = []

		#Converting string salaries to number salaries
		for salary in salaries:
			s = salary.replace("$","")
			s = s.replace(",","")
			s = s.replace(" ","")
			k = int(s)
			numberSalaries.append(k)

		# Writing to a file--creates if it deosn't exist
		with open(str(year) + "/" + position[0] + ".csv", 'w+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter = ',')
			for i in range(len(players)):
				filewriter.writerow([players[i], numberSalaries[i], position[1]])
