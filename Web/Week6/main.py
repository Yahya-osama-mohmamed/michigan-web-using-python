import json
import urllib.request, urllib.parse, urllib.error

import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0


url=input('enter url:')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_773278.json'

html = urllib.request.urlopen(url, context=ctx).read()
text= html.decode()

info = json.loads(text)


for item in info['comments']:
    sum=sum+int(item ['count'])
print (sum)     
    