import requests
res = requests.get('http://elasticsearch:9200')
print(res.content)
