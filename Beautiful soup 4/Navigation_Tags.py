import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#print(sauce) #print source code as it is
soup = bs.BeautifulSoup(sauce,"lxml")
nav = soup.nav 
#print(nav) #print all navigation tags
# for url in nav.find_all('a'):
# 	print(url.get('href')) #To print all links of a navigation bar of page
# body = soup.body
# for url in body.find_all('a'):
# 	print(url.get('href')) #To print all links of a navigation bar of page 
for div in soup.find_all('div'):
	print(div.text)  #print everything inside div as it is format without tags
	