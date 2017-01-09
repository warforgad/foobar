#!/bin/bash

echo "Killing old container..."
docker ps -q -f name=foobar_container | xargs docker rm -f
echo "Building image..."
docker build -t foobar .
echo "Running... "
docker run -tdi -v log:/log -p 8000:80 --name foobar_container foobar
docker ps -a
