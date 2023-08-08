FROM postgres:latest

MAINTAINER komob

ARG POSTGRES_DATABASE
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_ROOT_PASSWORD

ENV POSTGRES_DATABASE=$POSTGRES_DATABASE
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_ROOT_PASSWORD=$POSTGRES_ROOT_PASSWORD

ADD data.sql /etc/postgres/data.sql

RUN sed -i 's/POSTGRES_DATABASE/'$POSTGRES_DATABASE'/g' /etc/postgres/data.sql
RUN cp /etc/postgres/data.sql /docker-entrypoint-initdb.d

EXPOSE 5432