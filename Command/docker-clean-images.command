#!/bin/bash

for image_id in $(docker images -q | sort | uniq); do
    docker image rm $image_id -f
done
