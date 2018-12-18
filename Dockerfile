FROM ubuntu:latest
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3 curl git python3-pip
#RUN apt-get -y install nano
RUN pip3 install flask
RUN pip3 install requests
