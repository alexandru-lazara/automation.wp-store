#!/bin/bash

_file="docker/mysql/db-data.sql"
_database_container=mysql
_mysql_dump='exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"'

if [ "$(docker inspect -f '{{.State.Running}}' $_database_container)" == "true" ]; then
  docker exec $_database_container sh -c "$_mysql_dump" > $_file
  echo "MySQL dump creation successful."
else
  echo "Check if $_database_container is Running."
  echo "MySQL dump creation failed."
fi
