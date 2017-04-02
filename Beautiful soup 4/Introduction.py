import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#print(sauce) #print source code as it is
soup = bs.BeautifulSoup(sauce,"lxml")
##lxml is parser
#soup is more formatted source code form
#print(soup)
#print(soup.title.string) #return title name of web page
#print(soup.p) #print first p paragraph 
#print(soup.find_all('p') #print all p paragraph 
for paragraph in soup.find_all('p'):
	print(paragraph.string) #prints without tags
#there is certain difference b/w text & string
print(soup.get_text()) #print all web page in text form without tags 
for url in soup.find_all('a'):
	print(url.get('href')) #To print all links of a web page

 