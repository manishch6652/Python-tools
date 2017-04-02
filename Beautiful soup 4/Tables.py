import bs4 as bs
import urllib.request
import pandas as pd
# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# #print(sauce) #print source code as it is
# soup = bs.BeautifulSoup(sauce,"lxml")
# table = soup.table
# #print(table) #print first table
# table_rows = table.find_all('tr') # To find all table rows
# for tr in table_rows: #print complete table in tabular format
# 	td = tr.find_all('td')
# 	row = [i.text for i in td] 	
# 	#print(row)
# #part 2 Reading tables using pandas
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header = 0)
# for df in dfs:
# 	print(df)
#part3 parse xml
sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce,"xml")
#print(soup) #print xml code
for url in soup.find_all('loc'):
	print(url.text)
