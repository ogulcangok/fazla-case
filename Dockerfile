FROM tiangolo/uwsgi-nginx-flask:python3.10
ENV UWSGI_INI uwsgi.ini
ENV LISTEN_PORT 5000
EXPOSE 5000


WORKDIR /application
COPY requirements.txt /application/requirements.txt



RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /application
