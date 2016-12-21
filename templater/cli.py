# -*- coding: utf-8 -*-

import click
from templater import get_json, open_json, template_factory


# TODO: Allow basic authentication
# TODO: Add ability to pass in GET parameters or query string

@click.command()
@click.argument('data')
@click.argument('template_file')
def main(data, template_file, args=None):
    """Pipe JSON data into Jinja2 templates"""
    if 'http://' in data:
        json_data = get_json(data)
        out = template_factory(json_data, template_file)
    else:
        json_data = open_json(data)
        out = template_factory(json_data, template_file)

    click.echo(out)


if __name__ == "__main__":
    main()
