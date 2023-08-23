#!/usr/bin/env python
# coding: utf-8

from influxdb import InfluxDBClient

try:
    host = '192.168.1.120'
    port = '8086'
    name = 'paas4ml'
    pwd = 'paas4ml'
    db = 'k8s-metric'
    influxdb_mgr = InfluxDBClient(host=host, port=port, username=name, password=pwd, database=db)
except Exception as exp:
    print(str(exp))

query = 'show measurements'
result = influxdb_mgr.query(query)
node_metric = {}
for table in result.get_points():
    tname = table['name']
    if 'k8s-cluster-resource' in tname:
        if tname not in table.keys():
            node_metric[tname] = {'cpu':[], 'memory':[], 'last':{'cpu':0, 'memory':0, 'time':''}}
    elif 'k8s-pod-resource' in tname:
        if tname not in table.keys():
            node_metric[tname] = {'cpu':[], 'memory':[], 'last':{'cpu':0, 'memory':0, 'time':''}}


for metric in node_metric.keys():
    query = 'SELECT * FROM "{tnm}" WHERE time >= now() - 10s and time <= now();'.format(tnm=metric)
    result = influxdb_mgr.query(query)
    
    mtime = ''
    for point in result.get_points():
        mtime = point['time']
        node_metric[metric]['cpu'].append(point['cpu'])
        node_metric[metric]['memory'].append(point['memory'])
    node_metric[metric]['last']['cpu'] = node_metric[metric]['cpu'][-1]
    node_metric[metric]['last']['memory'] = node_metric[metric]['memory'][-1]
    node_metric[metric]['last']['time'] = mtime
