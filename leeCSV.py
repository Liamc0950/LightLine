import urllib.request
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as BS
import csv
import re

URL = "https://www.leefilters.com/lighting/colour-list.html"

page = 0
limit = 0

fullNames = []
codes = []
colorValues = []



req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
	html = response.read()
	soup = BS(html, features="html.parser")

	codeSoup = soup.findAll("a", {"class": "name"})

	for i in range (len(codeSoup) - 13 ):
		code = codeSoup[i]
		print(re.sub(";", "", re.sub("#", "", code["style"].split(":")[1])))
		colorValues.append(re.sub(";", "", re.sub("#", "", code["style"].split(":")[1])))
		fullNames.append(' '.join(code.contents[0].split(" ")[1:]))
		codes.append('L' + code.contents[0].split(" ")[0])



with open('lee.csv', mode='w') as lee_file:
	lee_writer = csv.writer(lee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	j = 0
	lee_writer.writerow(["COLOR CODE", "COLOR NAME", "HEX VALUE"])
	while j < len(fullNames):
		lee_writer.writerow([codes[j], fullNames[j], colorValues[j]])
		j += 1