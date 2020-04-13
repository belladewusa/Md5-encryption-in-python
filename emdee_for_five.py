import requests
import re
import hashlib


url = "The url is from a CTFs platform challenge"

### Get request
r= requests.session()
x = r.get('The url is from a CTFs platform challenge')
x = re.search("<h3 align='center'>+.*?</h3>", x.text)

### Remove unnecessary informations
x = re.search(">.*<", x[0])
x = re.search("\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w",x[0])

### Encode our given hash!
x = hashlib.md5(x[0].encode('utf-8')).hexdigest()

### Post request
data={'hash': x}
x = r.post(url = url, data = data)

print(x.text)


