#!/bin/bash

echo "[LOG] Init mysql server with docker"
docker pull mysql
docker run --name isteam-web-mysql -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=isteam -p 3306:3306 -d mysql
