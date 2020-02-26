FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY requirements.txt /tmp/
COPY ./data /data
RUN pip install -r /tmp/requirements.txt && \
	rm /tmp/requirements.txt
COPY ./app /app