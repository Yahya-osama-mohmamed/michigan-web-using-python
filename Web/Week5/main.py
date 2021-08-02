import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url = 'http://py4e-data.dr-chuck.net/comments_773277.xml'
html = urllib.request.urlopen(url, context=ctx).read()
text= html.decode()
tree= ET.fromstring(text)
counts =  tree.findall('.//count')
for count  in counts :
    sum=sum+int(count.text)

 
print(sum)