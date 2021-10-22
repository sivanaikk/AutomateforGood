FROM python:3.8
LABEL maintainer="Automate for Good@Team"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install net-tools -y
EXPOSE 5000

ENTRYPOINT cd UI && flask run --host 0.0.0.0 