import requests
from elasticsearch import Elasticsearch
import json

res = requests.get('http://elasticsearch:9200')
print(res.content)


es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

r = requests.get('http://elasticsearch:9200')
i = 1
while r.status_code == 200:
    r = requests.get('https://swapi.dev/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1

print(i)

es.get(index='sw', doc_type='people', id=5)

r = requests.get('http://elasticsearch:9201')
i = 18
while r.status_code == 30:
   r = requests.get('https://swapi.dev/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
   i=i+1

es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})


es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})
