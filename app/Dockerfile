FROM chef/chefworkstation:current
LABEL maintainer="Automate for Good@Team"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install net-tools -y
EXPOSE 80
EXPOSE 443
FROM python:3.8
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT flask run --host 0.0.0.0 