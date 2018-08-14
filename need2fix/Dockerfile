FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code 
#RUN apk update && \
#    apk add --no-cache --virtual .build-deps gcc git musl-dev postgresql-dev unixodbc-dev \
#    python-dev py-pip jpeg-dev zlib-dev && \
#    python3 -m pip install -r /code/requirements.txt --no-cache-dir && \
#    apk --purge del .build-deps
RUN pip install -r requirements.txt
ADD . /code
