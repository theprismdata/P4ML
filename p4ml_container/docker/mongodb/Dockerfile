FROM mongo:4.2

ARG BUILD_PATH
ADD $BUILD_PATH/mongo-init.js /docker-entrypoint-initdb.d/mongo-init.js
