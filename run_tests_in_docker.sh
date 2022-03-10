#! /bin/sh -eu

docker_image=pytest-with-src:v1
docker-compose down --remove-orphans --rmi local || true
docker-compose up -d --scale chrome=2 --scale firefox=2
docker build -t ${docker_image} -f Dockerfile .
docker run --network="host" --rm ${docker_image} --browser "chrome" --executor "remote" -m "sanity_test"
docker rmi ${docker_image}
docker-compose down --remove-orphans --rmi local


