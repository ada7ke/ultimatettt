#!/bin/sh
image=ultimatettt

echo "Restarting containers with image name $image"

echo "Stopping container"
# Stop the container
docker stop $(docker ps -q -f ancestor=$image)

echo "Removing container"
# Remove the container
docker rm $(docker ps -a -q -f ancestor=$image)

echo "Starting container"
# Start a new container with the latest image
docker run -d --restart unless-stopped -p 39030:8501 $image

echo "Done"
