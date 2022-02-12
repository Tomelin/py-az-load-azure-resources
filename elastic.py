import requests
from elasticsearch import Elasticsearch
import json

res = requests.get('http://elasticsearch:9200')
print(res.content)

es = Elasticsearch("http://elasticsearch:9200")

data = [{"balance": "$2,410.62", "age": 40, "name": "Bettie Buckner", "gender": "female", "company": "RODEOMAD",
         "email": "bettiebuckner@rodeomad.com", "phone": "+1 (857) 491-2461"},
        {"balance": "$1,143.56", "age": 28, "name": "Hanson Gates", "gender": "male", "company": "PEARLESSA",
         "email": "hansongates@pearlessa.com", "phone": "+1 (825) 524-3896"},
        {"balance": "$2,542.95", "age": 20, "name": "Audra Marshall", "gender": "female", "company": "COMTRAIL",
         "email": "audramarshall@comtrail.com", "phone": "+1 (920) 569-2780"},
        {"balance": "$2,235.86", "age": 34, "name": "Milagros Conrad", "gender": "female", "company": "IDEGO",
         "email": "milagrosconrad@idego.com", "phone": "+1 (823) 451-2064"},
        {"balance": "$2,606.95", "age": 34, "name": "Maureen Lopez", "gender": "female", "company": "EVENTEX",
         "email": "maureenlopez@eventex.com", "phone": "+1 (913) 425-3716"}]
for a_data in data:
    res = es.index(index='my-index', body=a_data)
    print(res)

r = requests.get('http://elasticsearch:9200')
i = 1
while r.status_code == 5:
    r = requests.get('https://swapi.dev/api/people/'+ str(i))
    es.index(index='sw',  id=i, body=json.loads(r.content))
    i=i+1

print(i)

es.get(index='sw', id=5)

r = requests.get('http://elasticsearch:9200')
i = 18
while r.status_code == 30:
   r = requests.get('https://swapi.dev/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
   i=i+1

es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})


es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})
