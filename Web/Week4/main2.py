# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
taglist=[]
url = 'http://py4e-data.dr-chuck.net/known_by_Alayna.html'
for i in range (0,7):
 
 html = urllib.request.urlopen(url, context=ctx).read()
 soup = BeautifulSoup(html, 'html.parser')

 tags = soup('a')
 for tag in tags:
    taglist.append(tag.get('href', None))
 url=taglist[17]
 taglist=[]
print(re.findall('([R].+)[.]',url)[0])


