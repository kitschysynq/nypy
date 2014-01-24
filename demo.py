#!/usr/bin/env python

import digitalocean
import os
from pprint import pprint
import redis


def dump(hash):
	pprint([ vars(x) for x in hash])


drop_info = {
		'client_id': os.environ['CLIENT_ID'],
		'api_key': os.environ['API_KEY'],
		'region_id': 4,
		'size_id': 66,
		'image_id': 1979326,
		'ssh_key_ids': 61401
		}

droplets = []
for i in range(5):
	drop_info['name'] = 'nypy' + str(i)
	droplets.append(digitalocean.Droplet(**drop_info))
	print "Creating droplet " + droplets[-1].name
	droplets[-1].create()

r = redis.Redis("107.170.0.146")

for d in droplets:
	event = None
	while event is None:
		d.load()
		event = d.get_events()
	print d.name, d.ip_address
	while(event[0].percentage != "100"):
		print event[0].percentage
		event[0].load()
	r.rpush("frontend:pydemo.baker.es", "http://" + d.ip_address + ":80")

