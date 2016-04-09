import wikipedia
#import requests
import urllib2
from bs4 import BeautifulSoup 
#import BeautifulSoup4

def getCompanies():
	companies = []
	wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
	header = {'User-Agent': 'Mozilla/7.0'}
	request = urllib2.Request(wikiLink, headers=header)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page, "lxml")
	table = soup.find("table", {"class": "wikitable sortable"})
	g = table.find_all("td")
	#h = g.find("a href")
	#print(h);
	#cell = [company.text for company in soup.findAll('tr')]
	#print(cell)
	for row in table.findAll("tr"):
		#cell = row.find.findAll("td").text
		#print(type(row.text))
		#print(row.text)
		cell = [row.text]
		g = cell[0].split("\n")
		companies.append(str(g[2]))
	
	return companies

def getCompanyData(companies):
	wikiContent = []

	for company in companies:
		try:
			pageContent = wikipedia.page(company).content
			wikiContent.append(pageContent)
		except:
			companies.remove(company)
	return wikiContent

def main():
	companies = getCompanies()
	#print 
	#print(len(companies))
	companyData = getCompanyData(companies)
	print(len(companyData))
	print(len(companies))
	#print(wikiContent)



main()