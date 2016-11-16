# -*- coding: utf-8 -*-

import click
from templater import *


@click.command()
@click.argument('data', help="JSON data file or a url from which to fetch JSON data")
@click.argument('template_file', help="Full path to the Jinja2 template file")
def main(data, template_file):
    """Pipe JSON data into Jinja2 templates"""
    if 'http://' in data:
        json_data = get_json(data)
        create = template_factory(data)
        out = create(template_file)
    else:
        json_data = open_json(data)
        create = template_factory(data)
        out = create(template_file)

    click.echo(out)


if __name__ == "__main__":
    main()
