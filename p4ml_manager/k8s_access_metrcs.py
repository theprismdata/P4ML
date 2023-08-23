#!/usr/bin/env python
# coding: utf-8


from kubernetes import client, config
import json
import os
from influxdb import InfluxDBClient

"""
Grafana
http://192.168.1.120:3000/
id : admin
pwd : paas4ml
"""

try:
    host = '192.168.1.120'
    port = '8086'
    name = 'paas4ml'
    pwd = 'paas4ml'
    db = 'k8s-metric'
    influxdb_mgr = InfluxDBClient(host=host, port=port, username=name, password=pwd, database=db)
except Exception as exp:
    print(str(exp))

config.load_kube_config()
api = client.CustomObjectsApi()

kubeconfig = os.getenv('KUBECONFIG')
config.load_kube_config(kubeconfig)
v1 = client.CoreV1Api()
api_client = client.ApiClient()

while True:
    k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
    fields = {'cpu': '', 'memory': ''}
    for stats in k8s_nodes['items']:
        table_name = 'k8s-cluster-resource-%s' % (stats['metadata']['name'])
        fields['cpu'] = int(stats['usage']['cpu'][:-1])
        fields['memory'] = int(stats['usage']['memory'][:-2])
        influx_json = [{'measurement': table_name, 'fields': fields}]

        if influxdb_mgr.write_points(influx_json) is True:
            # print('influx write success:' + str(influx_json))
            pass
        else:
            print('influx write faile:' + str(influx_json))

        ret_metrics = api_client.call_api('/apis/metrics.k8s.io/v1beta1/namespaces/default/pods', 'GET',
                                          auth_settings=['BearerToken'], response_type='json', _preload_content=False)
        response = ret_metrics[0].data.decode('utf-8')

        metric_info = json.loads(response)
        # print(metric_info)

    for idx, pod_id in enumerate(metric_info['items']):
        name = metric_info['items'][idx]['containers'][0]['name']
        cpu_n = int(metric_info['items'][idx]['containers'][0]['usage']['cpu'][:-1])
        memory_n = int(metric_info['items'][idx]['containers'][0]['usage']['memory'][:-2])
        # print(name, cpu_n, memory_n)
        fields = {'cpu': '', 'memory': ''}
        fields['cpu'] = cpu_n
        fields['memory'] = memory_n
        table_name = 'k8s-pod-resource-%s' % (name)
        influx_json = [{
            'measurement': table_name,
            'fields': fields
        }]
        if influxdb_mgr.write_points(influx_json) is True:
            # print('influx write success:' + str(influx_json))
            pass
        else:
            print('influx write faile:' + str(influx_json))

