"""
    HTTP Requests
    pip install requests
"""

import requests
import json

api_key = "31c21508fad64116acd229c10ac11e84"
url = "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}".format(api_key)

response = requests.get(url)
text = response.text

print(text)
print(type(text))

# converted JSON textual content as Python Dictionary
data = json.loads(text)
print(data)
print(type(data))

print(data['totalResults'])
print()
for article in data['articles']:
    print(article['title'])
    print(article['author'])
    print()