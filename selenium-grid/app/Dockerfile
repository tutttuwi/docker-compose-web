FROM python:3.8
 
RUN apt-get -y update && \
    python -m pip install --upgrade pip
 
ADD requirements.txt .
 
RUN pip install -r requirements.txt
 
WORKDIR /app