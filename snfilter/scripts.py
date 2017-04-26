#! /usr/bin/env python

import sys
import json
import click
import logging
import requests

log = logging.getLogger(__name__)

from snfilter import parse_nameslist

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

@cli.command()
@click.option("--filename", default="grfeed.txt", help="file containing the sn gr feed to parse")
@click.option("--nameslist", default="kf5uxa:Matt Dipirro,W5ZFQ:Andrew,Daniel Shaw", help="list of names to include in the filtered output")
def filter(filename, nameslist):
    with open(filename, "r") as f:
        d = "".join([ l for l in f.readlines() ])
        names, xlator = parse_nameslist(nameslist)
        f = filter_feed(d, names, translator=xlator)
