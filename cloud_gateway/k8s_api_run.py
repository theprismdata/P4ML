import json

from flask import Flask, jsonify
from kubernetes import client, config
import os
from influxdb import InfluxDBClient

kubeconfig = os.getenv('KUBECONFIG')
config.load_kube_config(kubeconfig)
v1 = client.CoreV1Api()

try:
    host = '192.168.1.120'
    port = '8086'
    name = 'paas4ml'
    pwd = 'paas4ml'
    db = 'k8s-metric'
    influxdb_mgr = InfluxDBClient(host=host, port=port, username=name, password=pwd, database=db)
except Exception as exp:
    print(str(exp))

def get_list_pod_for_all_namespaces(handler):
    ret = v1.list_pod_for_all_namespaces(watch=False)
    pods_list =ret.items
    res_list = []
    for pod in pods_list:
        pod = pod.to_dict()
        ns = pod['metadata']['namespace']
        if 'app' in pod['metadata']['labels'].keys():
            name = pod['metadata']['labels']['app']
        res_list.append({'ns':ns, 'name':name})
    return res_list

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
@app.route('/')
@app.route('/index')
def index():
    resp = jsonify(success=True)
    return resp

@app.route('/k8s_private_get_list_pod_for_all_ns', methods=['GET'])
def list_pod_for_all_namespaces():
    res_list = get_list_pod_for_all_namespaces(v1)
    resp = jsonify(success=True, response=res_list)
    return resp


def get_all_metric_all_namespaces():
    query = 'show measurements'
    result = influxdb_mgr.query(query)

    node_metric = {'cluster_metric': {}, 'pod_metric': {}}
    for table in result.get_points():
        tname = table['name']
        if 'k8s_cluster_resource' in tname.replace('-', '_'):
            if tname not in table.keys():
                name_ = tname.replace('-', '_')
                node_metric['cluster_metric'][name_] = {'cpu': [], 'memory': [],
                                                        'last': {'cpu': 0, 'memory': 0, 'time': ''}}
        elif 'k8s_pod_resource' in tname.replace('-', '_'):
            if tname not in table.keys():
                name_ = tname.replace('-', '_')
                node_metric['pod_metric'][name_] = {'cpu': [], 'memory': [],
                                                    'last': {'cpu': 0, 'memory': 0, 'time': ''}}

    for section in node_metric.keys():
        for metric in node_metric[section].keys():
            print(section, metric)
            query = 'SELECT * FROM "{tnm}" WHERE time >= now() - 10s and time <= now();'.format(
                tnm=metric.replace('_', '-'))
            result = influxdb_mgr.query(query)
            for point in result.get_points():
                mtime = point['time']
                node_metric[section][metric]['cpu'].append(point['cpu'])
                node_metric[section][metric]['memory'].append(point['memory'])
            node_metric[section][metric]['last']['cpu'] = node_metric[section][metric]['cpu'][-1]
            node_metric[section][metric]['last']['memory'] = node_metric[section][metric]['memory'][-1]
            node_metric[section][metric]['last']['time'] = mtime
    return node_metric


@app.route('/k8s_private_all_metric', methods=['GET'])
def get_metric_all_namespaces():
    res_list = get_all_metric_all_namespaces()
    resp = jsonify(success=True, response=res_list)
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
