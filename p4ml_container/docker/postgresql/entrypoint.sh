#!/bin/bash

echo "entrypoint.sh run"
POSTGRESQL_BIN=/usr/lib/postgresql/13/bin/postgres
POSTGRESQL_CONFIG_FILE=/etc/postgresql/13/main/postgresql.conf
echo $POSTGRESQL_BIN
echo $POSTGRESQL_CONFIG_FILE

POSTGRESQL_SINGLE="sudo -u postgres $POSTGRESQL_BIN --single  --config-file=$POSTGRESQL_CONFIG_FILE"

$POSTGRESQL_SINGLE <<< "ALTER USER postgres PASSWORD 'paas4ml';" > /dev/null
echo $POSTGRESQL_SINGLE

exec sudo -u postgres $POSTGRESQL_BIN --config-file=$POSTGRESQL_CONFIG_FILE
