# PaaS4ML

### 프로젝트 목적
1. 클라우드 환경에서 동작하는 Machine Learning Platform 구축을 목적으로 합니다.
2. 접근 및 사용이 용이하도록 합니다.
3. Kubernetes / AWS / NaverBusinessPlatform에서 동작하는 것을 목적으로 합니다.

![](\feature\front1.png)

### 주요 구성 요소
1. p4ml_container
   1. 데이터 저장소(Postgresql, Influxdb, MongoDB) 배포를 목적으로 합니다. 
   2. 시각화 도구(Grafana) 배포를 목적을 합니다.
   3. 웹기반 Python 개발환경(Jupyter notebook) 배표를 목적을 합니다.
      1. python container에는 다양한 예제가 포함됩니다.
      
2. p4ml_container
   1. Machine Learning 모델 개발과 서비스를 위한 패키지 배포를 목표로 합니다.
   
3. mlops_component
   1. ML ops 배포를 목적으로 합니다.

4. p4ml_manager
   1. 클라우드 제어/모니터링을 수행합니다.
   2. Machine Learning 개발환경, 데이터 저장소에 접근 가능한 주소를 보여줍니다.
   3. 로그인
      4. ID : admin Password: paas4ml

5. 각 container 실행 방법
   1. kubernetes 환경
      1. Pod 설치/실행
         1. Metallb 설치<br>
            1). 한번에 설치
               kubectl apply -f metallb_setup\metallb-setup.yaml <br>
            2). 개별 요소 설치
               kubectl apply -f metallb_setup\namespace.yaml
               kubectl apply -f metallb_setup\config.yaml
               kubectl apply -f metallb_setup\metallb.yaml <p>
          
         2. Jupyter notebook <br>
               kubectl apply -f p4ml_container/k8s/jupyter/jupyter-metallb.yaml
         3. Grafana <br>
            kubectl apply -f p4ml_container/k8s/grafana/grafana-metallb.yaml
         4. Influxdb  <br>
            kubectl apply -f p4ml_container/k8s/influxdb/influxdb-metallb.yaml
         5. Mongodb <br>
            kubectl apply -f p4ml_container/k8s/mongo/mongodb-metallb.yaml
         6. PostgreSQL  <br>
            kubectl apply -f p4ml_container/k8s/postgres/postgres-metallb.yaml
         7. Minio  <br>
            kubectl apply -f p4ml_container/k8s/minio/minio-metallb.yaml
         8. 전체 Pod 한번에 설치 <br>
            p4ml_container/k8s로 이동
            chmod +x k8s-apply.sh
            ./k8s-apply.sh
   
      3. kubernetes에서 각 구성 요소 접근 방법
         1. Jupyter Notebook 
            1. IP : 192.168.1.151 Port : 8888
            2. Password : paas4ml
   
         2. Grafana
            1. IP : 192.168.1.150 Port : 3000
            2. ID : admin / Password : paas4ml
      
         3. InfluxDB
            1. IP : 192.168.1.154 Port : 8086
            2. Database : paas4ml
            3. ID : admin / Password : paas4ml
      
         4. MongoDB
            1. IP : 192.168.1.152 Port : 27017
            2. Database : paas4ml
            3. ID : admin / Password : paas4ml
      
         5. Postgresql
            1. IP : 192.168.1.153 Port : 5432
            2. Database : postgresdb
            3. ID : postgresadmin / Password : paas4ml

         6. MinIO
            1. IP : 192.168.1.155 Port : 9000
            2. Database : postgresdb
            3. ID : minio / Password : minio123
      
   2. Docker 환경(Windows)
      1. Docker Compose로 컨테이너 실행
         1. docker-compose -f p4ml_container/docker/docker-compose.yaml up -d <br>
            구성요소 : Jupyter Notebook, Grafana, InfluxDB, MongoDB, PostgreSQL, Minio
         2. Jupyter Notebook:
            1. URL  : http://localhost:8888/tree
            2. Password : paas4ml
         3. Grafana:
            1. URL : http://localhost:3000/login
            2. ID : admin / Password : paas4ml
         4. InfluxDB:
            1. URL : localhost:8086
            2. Database : paas4ml
            3. ID : admin / Password : paas4ml
         5. MongoDB:
            1. URL : localhost:27017
            2. Database : paas4ml
            3. ID : admin / Password : paas4ml
         6. PostgreSQL:
            1. URL : localhost:5432
            2. Database : postgresdb
            3. ID : postgresadmin / Password : paas4ml
            
      2. 개별 docker로 실행
         1. Influxdb: <br>
            1. docker run -d -e DOCKER_INFLUXDB_INIT_MODE=setup -e DOCKER_INFLUXDB_INIT_USERNAME=admin -e DOCKER_INFLUXDB_INIT_PASSWORD=paas4ml -v .\share_volume\influxdb_data:/var/lib/influxdb --name p4ml_influxdb -p 8086:8086 prismdata/p4ml_influxdb
         2. Grafana: <br>
            1. docker run -d -e GF_SECURITY_ADMIN_USER=admin -e GF_SECURITY_ADMIN_PASSWORD=paas4ml -e GF_INSTALL_PLUGINS= -v .\share_volume\grafana_data:/var/lib/grafana --name p4ml_grafana -p 3000:3000 prismdata/p4ml_grafana
         3. Mongodb: <br>
            1. docker run -d -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=paas4ml -e MONGO_INITDB_DATABASE=paas4ml -v .\share_volume\mongodb_data:/data/db --name p4ml_mongodb -p 27017:27017 prismdata/p4ml_mongodb
         4. Jupyter: <br>
            1. docker run -d --name p4ml_jupyter -p 8888:8888 -v .\share_volume\jupyter_data:/example/workdir prismdata/p4ml_jupyter  
         5. PostgreSQL: <br>
            1. run: docker run -d -e POSTGRES_USR=postgres -e POSTGRES_PASSWORD=paas4ml -v .\share_volume\postgresql_data\data:/var/lib/postgresql/data -v .\share_volume\postgresql_data\log:/var/log/postgresql --name p4ml_postgres  -p 5432:5432  prismdata/p4ml_postgresql
         6. Host는 각 Container이름으로 접속
         [k8s_api](infra_api_test%2Fk8s_api)
6. Kubernetis NFS
   1. Pod의 데이터 보존과 접근을 위해 각 Worker 노드에 저장된 데이를 Master에서 접근할 수 있도록 Network Drive를 구성합니다. 
      1. Master Node
         1. nfs 설치
           ```jsx
            yum -y install nfs-utils
           ```
         2. 서비스 시작 / 부팅 시 자동 시작
           ```jsx
             systemctl start nfs-server
             systemctl start rpcbind
             systemctl enable nfs-server
             systemctl enable rpcbind
           ```
         3. 공유할 디렉토리 생성
         ```jsx
         mkdir -p /root/pod_storage/grafana_data
         mkdir -p /root/pod_storage/mongo_data
         mkdir -p /root/pod_storage/jupyter_data
         ```
         4. vi /etc/exports
         ```jsx
         /root/pod_storage/grafana_data 192.168.1.*(rw,no_root_squash,sync)
         /root/pod_storage/grafana_data worker1(rw,no_root_squash,sync)
         /root/pod_storage/grafana_data worker2(rw,no_root_squash,sync)
         /root/pod_storage/grafana_data worker3(rw,no_root_squash,sync)
         /root/pod_storage/mongo_data 192.168.1.*(rw,no_root_squash,sync)
         /root/pod_storage/mongo_data worker1(rw,no_root_squash,sync)
         /root/pod_storage/mongo_data worker2(rw,no_root_squash,sync)
         /root/pod_storage/mongo_data worker3(rw,no_root_squash,sync)
         /root/pod_storage/jupyter_data 192.168.1.*(rw,no_root_squash,sync)
         /root/pod_storage/jupyter_data worker1(rw,no_root_squash,sync)
         /root/pod_storage/jupyter_data worker2(rw,no_root_squash,sync)
         /root/pod_storage/jupyter_data worker3(rw,no_root_squash,sync)
         ```
         5. 서비스 재시작
          ```jsx
          systemctl restart nfs-server
          ```
         6. 설정 확인
          ```jsx
          exportfs -a
          exportfs -v
          ```

      2. Worker Node
         1. nfs 설치
         ```jsx
         yum -y install nfs-utils
         ```
      3. 서비스 시작 / 부팅 시 자동 시작
         ```jsx
         systemctl start nfs-server
         systemctl enable nfs-server
         ```
      4. mount 즉시 적용
         서버의 /root/pod_storage/~ 디렉토리를 로컬 /*mnt/~*에 마운트*
         ```jsx
         mount -t nfs 192.168.1.100:/root/pod_storage/grafana_data /mnt/grafana_data
         mount -t nfs 192.168.1.100:/root/pod_storage/mongo_data /mnt/mongo_data 
         mount -t nfs 192.168.1.100:/root/pod_storage/jupyter_data /mnt/jupyter_data
         ```
      5. mount 영구 적용
         ```jsx
         vi /etc/fstab
         192.168.1.100:/root/pod_storage/grafana_data /mnt/grafana_data	nfs	defaults	0 0
         192.168.1.100:/root/pod_storage/mongo_data /mnt/mongo_data 	nfs	defaults	0 0
         192.168.1.100:/root/pod_storage/jupyter_data /mnt/jupyter_data nfs	defaults	0 0
         ```
         
Used license <br>
Mictronics GaugeMeter  MIT license <br>
Flask-datta-able MIT License <br>