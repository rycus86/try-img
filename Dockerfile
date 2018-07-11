FROM alpine

RUN apk add --no-cache python2 py2-pip

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD app.py /var/app/app.py

CMD python /var/app/app.py

