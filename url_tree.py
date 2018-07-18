#! python3

import requests, sys, webbrowser, bs4

print('Searching....')

#the search term is thrown by sys.argv 
#usage: python url_tree.py "worldcup"
get_url_info = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))

# check status
get_url_info.raise_for_status()

# create bs4 object
bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'html.parser')

# extract only search results
linkElems = bs4Obj.select('.r a')

# the maximum number of webpages is 5
num = min(5, len(linkElems))

# open web page
[webbrowser.open('http://google.com' + linkElems[i].get('href')) for i in range(num)]

print('end search')