FROM python:3.6

ADD . /www
WORKDIR /www
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && \
	pip install -r /tmp/requirements.txt && \
	rm /tmp/requirements.txt
CMD uwsgi uwsgi.ini