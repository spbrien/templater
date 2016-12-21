# Templater

Render Jinja2 templates using JSON data

## Requirements

pip

## Installation

From the directory this file is in:
```
pip install -e ./
```

## Usage

This tool passes JSON formatted data into Jinja2 templates, then renders the result out to the console. Result can also be written to a file.

#### JSON File
```
templater file.json my_jinja2_template.html
templater file.json my_jinja2_template.html > out.html
```

#### JSON API Endpoint
```
templater http://my-json-api.com/endpoint my_jinja2_template.html
templater http://my-json-api.com/endpoint my_jinja2_template.html > out.html
```
