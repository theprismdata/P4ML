mkdir share_volume\jupyter_data
docker run -d --name p4ml_jupyter -p 8888:8888 -v .\share_volume\jupyter_data:/example/workdir 222.239.231.95:8093/pass4ml/p4ml_jupyter
docker network connect datastore_net p4ml_jupyter

mkdir share_volume\grafana_data
docker run -d -e GF_SECURITY_ADMIN_USER=admin -e GF_SECURITY_ADMIN_PASSWORD=paas4ml -e GF_INSTALL_PLUGINS= -v .\share_volume\grafana_data:/var/lib/grafana --name p4ml_grafana -p 3000:3000 222.239.231.95:8093/pass4ml/p4ml_grafana
docker network connect datastore_net p4ml_grafana

mkdir share_volume\influxdb_data
docker run -d -e DOCKER_INFLUXDB_INIT_MODE=setup -e DOCKER_INFLUXDB_INIT_USERNAME=admin -e DOCKER_INFLUXDB_INIT_PASSWORD=paas4ml -v .\share_volume\influxdb_data:/var/lib/influxdb --name p4ml_influxdb -p 8086:8086 222.239.231.95:8093/pass4ml/p4ml_influxdb
docker network connect datastore_net p4ml_influxdb

mkdir share_volume\postgresql_data
docker run -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=paas4ml -v .\share_volume\postgresql_data\data:/var/lib/postgresql/data -v .\share_volume\postgresql_data\log:/var/log/postgresql --name p4ml_postgres  -p 5432:5432  222.239.231.95:8093/pass4ml/p4ml_postgres
docker network connect datastore_net p4ml_postgres

mkdir share_volume\mongodb_data
docker run -d -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=paas4ml -e MONGO_INITDB_DATABASE=paas4ml -v .\share_volume\mongodb_data:/data/db --name p4ml_mongodb -p 27017:27017 222.239.231.95:8093/pass4ml/p4ml_mongodb
docker network connect datastore_net p4ml_mongodb

mkdir share_volume\minio-data
docker run -d -p 9000:9000 -p 9001:9001 --name p4ml_minio  -v ~/share_volume/minio-data:/data -e "MINIO_ROOT_USER=minio" -e "MINIO_ROOT_PASSWORD=minio123"  quay.io/minio/minio server /data --console-address ":9001"
docker network connect datastore_net p4ml_minio