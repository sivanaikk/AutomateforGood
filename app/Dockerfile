FROM chef/chefworkstation:current
LABEL maintainer="Automate for Good@Team"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install net-tools -y
EXPOSE 80
EXPOSE 443
RUN apt-get install python3.8 -y 
RUN apt-get install python3-pip -y
RUN pip3 install -r /app/requirements.txt
EXPOSE 5000
ENTRYPOINT flask run --host 0.0.0.0 