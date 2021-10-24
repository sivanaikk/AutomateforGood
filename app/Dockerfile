FROM chef/chefworkstation:current
LABEL maintainer="Automate for Good@Team"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install net-tools -y
RUN apt-get install python3.8 -y 
RUN apt-get install python3-pip -y
RUN pip3 freeze > requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 80
EXPOSE 443
EXPOSE 5000
WORKDIR /app/AutomateForGood-UI
CMD flask run --host 0.0.0.0 
