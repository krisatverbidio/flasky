FROM python:3.10

ADD requirements.txt /tmp
RUN apt -y update && apt -y install net-tools
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir /app
COPY main.py /app
WORKDIR /app

CMD ["python", "/app/main.py"]
