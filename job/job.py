
import os
import json
import pika
import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import time
import subprocess

AZURE_SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
AZURE_CLIENT_ID = os.environ['AZURE_CLIENT_ID']
AZURE_CLIENT_SECRET = os.environ['AZURE_CLIENT_SECRET']
RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_PORT = os.environ['RABBITMQ_HOST']
RABBITMQ_USER = os.environ['RABBITMQ_HOST']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_HOST']
ELASTICSEARCH_HOST = os.environ['ELASTICSEARCH_HOST']
ELASTICSEARCH_PORT = os.environ['ELASTICSEARCH_PORT']
ELASTICSEARCH_PROTOCOL = os.environ['ELASTICSEARCH_PROTOCOL']
ELASTICSEARCH_USER = os.environ['ELASTICSEARCH_USER']
ELASTICSEARCH_PASSWORD = os.environ['ELASTICSEARCH_PASSWORD']
LOOP_TIME  = os.environ['LOOP_TIME']

proc = subprocess.Popen(["./entrypoint2.sh"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

json_object = json.loads(out)

es = Elasticsearch("http://"+ELASTICSEARCH_HOST+":"+ELASTICSEARCH_PORT)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue='resources')
for song in json_object:
    song['timestamp'] = datetime.now()
    es.index(index='azure', doc_type='resources', body=json.loads(str(song)))
    channel.basic_publish(exchange='', routing_key='resources',body=str(song))
    connection.close()
    time.sleep(int(LOOP_TIME))
