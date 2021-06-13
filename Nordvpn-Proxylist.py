from bs4 import BeautifulSoup
from lxml import etree
import requests

URL = "https://nordvpn.com/ovpn/"
textfile = open("a_file.txt", "w")

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
			
			
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
list = dom.xpath('//span[@class="mr-2"]/text()')


for element in list:
    textfile.write("%s\n" % element)
textfile.close()