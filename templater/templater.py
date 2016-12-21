# -*- coding: utf-8 -*-

import os
import json

import requests
from requests.auth import HTTPBasicAuth
from jinja2 import FileSystemLoader, Environment


# Utility Functions
# -------------------------------

def template_factory(data, template_file):
    templates_dir = os.path.abspath(os.path.join(template_file, os.pardir))

    # Create template env
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(os.path.basename(template_file))

    # Render
    return template.render(data=data)


def open_json(json_file_path):
    with open(json_file_path, 'r') as data:
        return json.load(data)


def get_json(json_url, params={}, username=None, password=None):
    if username and password:
        r = requests.get(
            json_url,
            params=params,
            auth=HTTPBasicAuth(username, password)
        )
        return r.json()
    r = requests.get(json_url, params=params)
    return r.json()
