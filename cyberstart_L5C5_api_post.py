# CyberStart Level 5 Challenge 5 - "Jovian Tweets"

# POST method sent to that URL, with:
# - x-api-key:{KEY} in header
# - user={USER} in querystring
# - status-update={TEXT} in querystring
# ...creates a new social media post

import urllib.request

url = "http://127.0.0.1:8082"
values = {'user' : 'tweetbotuser',
    'status-update' : 'alientest'}
headers = {'x-api-key': 'tweetbotkeyv1'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)