import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import json
import requests, time




res = requests.get('http://elasticsearch:9200')
print(res.content)
i = 1
es = Elasticsearch("http://elasticsearch:9200")
es.ping()
es.index(index="my-index-000001", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

for i in range(100):
  es.index(index="python-index-000"+str(i), doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

r = requests.get('http://localhost:9200')

while r.status_code == 200:
    r = requests.get('https://swapi.dev/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    
  
print(i)

es.get(index='sw', doc_type='people', id=5)

r = requests.get('http://localhost:9200')
i = 18
while r.status_code == 200:
   r = requests.get('https://swapi.dev/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
   i=i+1
es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})
