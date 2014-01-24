#!/usr/bin/env python

import digitalocean
import os

mgr = digitalocean.Manager(client_id=os.environ['CLIENT_ID'], api_key=os.environ['API_KEY'])
droplets = mgr.get_all_droplets()

for d in droplets:
	if d.name.startswith('nypy'):
		d.destroy()
