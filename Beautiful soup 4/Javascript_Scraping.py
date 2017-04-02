import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,"lxml")
js_test = soup.find('p',class_ = 'jstest')
print(js_test.text)
