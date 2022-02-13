FROM python:alpine
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo make
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN adduser --disabled-password --shell /bin/sh --home /azuser azuser 

WORKDIR /azuser
COPY entrypoint.sh .
RUN chmod 0750 entrypoint.sh 
RUN chown azuser entrypoint.sh 
USER azuser
ENTRYPOINT ["/azuser/entrypoint.sh"]
