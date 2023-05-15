#!/bin/sh
image=ultimatettt

echo "Restarting containers with image name $image"

echo "Stopping container"
docker stop $(docker ps -q -f ancestor=$image)

echo "Removing container"
docker rm $(docker ps -a -q -f ancestor=$image)

echo "Building image"
docker build -t $image .

echo "Starting container $image"
docker run -d --restart unless-stopped -p 39030:8501 $image

echo "Done"
