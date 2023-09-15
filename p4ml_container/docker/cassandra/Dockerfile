FROM ubuntu:18.04

ARG BUILD_PATH
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y gnupg2
RUN apt-get install curl -y
RUN apt-get -y install sudo


RUN echo "deb https://debian.cassandra.apache.org 41x main" | tee /etc/apt/sources.list.d/cassandra.list
RUN curl https://downloads.apache.org/cassandra/KEYS | sudo apt-key add -

RUN apt-get update


ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sudo apt-get install cassandra -y

RUN sudo chmod 777 -R /var/log/cassandra
RUN sudo chmod 777 -R /var/lib/cassandra

ADD $BUILD_PATH/cassandra_docker.yaml /etc/cassandra/cassandra.yaml
EXPOSE 9042
RUN service cassandra start
