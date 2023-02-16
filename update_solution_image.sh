#!/bin/bash

PWD=$(pwd)

[[ "$PWD" != *django-workshop ]] && echo "Must call from project root" && exit

# Image name:tag.
image="emilte/django-workshop:solution"

# Build image.
docker build solution -t "$image"

# Push to hub.docker.com.
docker push "$image"
