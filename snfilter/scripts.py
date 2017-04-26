#! /usr/bin/env python

import sys
import json
import click
import logging
import requests

log = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--url", default="http://www.spotternetwork.org/feeds/gr.txt", help="SN Feed to pull")
@click.option("--filename", default="grfeed.txt")
def pull(url, filename):
    r = requests.get(url)
    if r.ok:
        log.debug("successfully requested %s", url)
        f = open(filename, "w")
        f.write(r.text)
        f.close()
    else:
        log.error("Request for %s failed.", url)
