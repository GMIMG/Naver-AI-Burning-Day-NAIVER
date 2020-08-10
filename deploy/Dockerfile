FROM tiangolo/uwsgi-nginx-flask:python3.6
ENV NGINX_MAX_UPLOAD 1m
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && \
	pip install -r /tmp/requirements.txt && \
	rm /tmp/requirements.txt
COPY ./app /app