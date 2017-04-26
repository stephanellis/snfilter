import requests
import sys
import json


gr_feed_preamble = """

Refresh: 1
Threshold: 999
Title: Spotter Network Positions - Filtered by Netmanager
Font: 1, 11, 0, "Courier New"
IconFile: 1, 22, 22, 11, 11, "http://www.spotternetwork.org/icon/spotternet.png"
IconFile: 2, 15, 25, 8, 25, "http://www.spotternetwork.org/icon/arrows.png"
IconFile: 6, 22, 22, 11, 11, "http://www.spotternetwork.org/icon/spotternet_new.png"

"""

def parse_nameslist(nameslist):
    names = list()
    xlator = dict()
    individuals = nameslist.split(",")
    for i in individuals:
        iparts = i.split(":")
        names.append(iparts[0])
        if len(iparts) == 2:
            xlator[iparts[0]] = iparts[1]
    return names, xlator

def filter_feed(raw_feed, names, translator=dict()):
    all_objects = parse_raw_feed(raw_feed)
    # filtered_objects = (invoke func that filteres the list based on names)
    # translated_objects = (invoke function that translates the names)
    # return filtered and translated list

def parse_objectlines(olines):
    log.debug("parsing a set of object lines")
    #parse the individual lines of the object
    #build up a datastructure of the elements
    ds = dict()
    ds["origlines"] = olines

    # these keys are for the TruVu csv output
    ds["Temperature"] = ""
    ds["Weather"] = ""
    ds["Station Name"] = ""
    for l in olines:
        if l.startswith("Object:"):
            oparts = l.split(":")
            if len(oparts) == 2:
                llparts = oparts[1].split(",")
                if len(llparts) == 2:
                    ds['Latitude'] = float(llparts[0])
                    ds['Longitude'] = float(llparts[1])
        if l.startswith("Text:"):
            tparts = l.split(",")
            if len(tparts) == 4:
                ds["name"] = tparts[3].strip('"').lstrip(" ").lstrip("\"")
                ds["Station Name"] = ds["name"] # TruVu CSV output
    return ds

def parse_raw_feed(raw):
    lines = raw.split("\n")
    # build up chunks of the data structure, we need to takes lines between
    # object and end and pass those to the chunk parser
    objects = list()
    objectlines = list()
    have_object = False
    for l in lines:
        log.debug("line is: \"%s\"", l)
        log.debug("have_object var is %s", have_object)
        l = l.strip()
        if l.startswith("Object:"):
            log.debug("have an object now")
            have_object = True
        if have_object:
            log.debug("adding line to object")
            objectlines.append(l)
            if l.startswith("End"):
                log.debug("end of object")
                have_object = False
                objects.append(parse_objectlines(objectlines))
                objectlines = list()
    return objects

def filter_objects_byname(objects, namelist, translator=dict()):
    lower_names = [ x.lower() for x in namelist ]
    filtered = list()
    for o in objects:
        if o["name"].lower() in lower_names:
            if o["name"] in translator:
                o["name"] = translator[o["name"]]
            filtered.append(o)
    return filtered
