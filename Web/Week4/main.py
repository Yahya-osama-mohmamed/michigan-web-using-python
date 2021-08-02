# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('ENTER:')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_773275.html'
    
html = urlopen(url ,context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numbers=[]
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    numbers=numbers+re.findall('[0-9]+', tag.decode())
sum=0
for num in numbers :
    sum=sum+int(num)
print (sum)     
