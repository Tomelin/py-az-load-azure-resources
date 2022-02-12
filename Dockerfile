FROM python:3

WORKDIR /app
COPY requirements.txt .
COPY elastic.py discovery_azure.py
#COPY discovery_azure.py .

RUN pip install -r requirements.txt 

CMD [ "python", "discovery_azure.py"]
