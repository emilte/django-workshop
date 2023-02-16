#!/bin/bash

PWD=$(pwd)

[[ "$PWD" != *django-workshop ]] && echo "Must call from project root" && exit

# Image name:tag.
image="emilte/django-workshop:clean"

# INSTALL=0 disables installation of dependencies to create a clean image.
docker build --build-arg INSTALL=0 solution -t "$image"

# Push to hub.docker.com.
docker push "$image"
