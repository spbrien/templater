# -*- coding: utf-8 -*-

import os
import json

import requests
from requests.auth import HTTPBasicAuth
from jinja2 import Template


# Utility Functions
# -------------------------------

def template_factory(data, template_path):
    def create_template(template_path):
        f = open(template_path, 'r')
        template_file = f.read()
        f.close()
        template = Template(template_file)
        out = template.render(data=data)
        return out
    return create_template


def open_json(json_file_path):
    with open(json_file_path, 'r') as data:
        return json.load(data)


def get_json(json_url, params={}, username=None, password=None):
    if username and password:
        r = requests.get(json_url, params=params, auth=HTTPBasicAuth(username, password))
        return r.json()
    r = requests.get(json_url, params=params)
    return r.json()
