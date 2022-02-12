FROM python:3

WORKDIR /app
COPY requirements.txt .
COPY elastic.py discovery_azure.py
#COPY discovery_azure.py .

RUN CERTIFICATE_VERIFY=false pip install -r requirements.txt config --global http.sslVerify false

CMD [ "python", "discovery_azure.py"]
