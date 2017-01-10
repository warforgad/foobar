#!/bin/bash

DB_CONTAINER='db_container'
APP_CONTAINER='foobar_container'

echo "Killing old db container..."
docker ps -aq -f name=$DB_CONTAINER | xargs docker rm -f
echo "Running db container... "
docker run --name $DB_CONTAINER -td -p 9000:5432 postgres
echo "Killing old container..."
docker ps -aq -f name=$APP_CONTAINER | xargs docker rm -f
echo "Building image..."
docker build -t foobar .
echo "Running... "
DB_IP=`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $DB_CONTAINER`
docker run -tdi -v log:/log -p 8000:80 --name $APP_CONTAINER --add-host="db_server:$DB_IP" foobar
docker ps -a
