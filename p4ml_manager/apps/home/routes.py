# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import requests

from apps.home import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


# @blueprint.route('/tbl_bootstrap_pod_list')
# @login_required
# def tbl_bootstrap_pod_list():
#     resonse = requests.get('http://192.168.1.100:5000/get_list_pod_for_all_ns')
#     pods = resonse.json()
#     resource_list = pods['response']
#     print(resource_list)
#     return render_template('home/tbl_bootstrap_pod_list.html', resource_list=resource_list)

@blueprint.route('/pod_ctrl', methods=["POST"])
def pod_ctrl():
    try:
        content = request.values.to_dict()
        print(content)
        resp = jsonify(success=True)
        return resp
    except Exception as e:
        resp = jsonify(success=False)
        return resp

@blueprint.route('/all_metric', methods=["GET"])
def all_metric():
    try:
        resonse = requests.get('http://192.168.1.100:5000/all_metric')
        metrics = resonse.json()
        return metrics
    except Exception as e:
        resp = jsonify(success=False)
        return resp

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        if segment == 'tbl_bootstrap_pod_list.html':
            resonse = requests.get('http://192.168.1.100:5000/get_list_pod_for_all_ns')
            pods = resonse.json()
            resource_list = pods['response']
            print(resource_list)
            return render_template('home/tbl_bootstrap_pod_list.html', resource_list=resource_list)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
