#! /bin/bash

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t apartment-finder .
docker run -d -v /home/ubuntu/apartment-finder/config:/opt/wwc/apartment-finder/config apartment-finder