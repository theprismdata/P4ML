FROM ubuntu:18.04

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y gnupg2
RUN apt-get install wget -y
RUN apt-get -y install sudo

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add -

RUN apt-get update
RUN apt-get upgrade
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get install -y  postgresql-13 postgresql-contrib

WORKDIR /etc/postgresql/13/main
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" postgresql.conf
RUN echo "host all all 0.0.0.0/0 password" >> pg_hba.conf

EXPOSE 5432
ARG BUILD_PATH

ADD $BUILD_PATH/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh

