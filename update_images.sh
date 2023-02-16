#!/bin/bash

PWD=$(pwd)

[[ "$PWD" != *django-workshop ]] && echo "Must call from project root" && exit

./update_clean_image.sh
./update_solution_image.sh
