import json
import re

with open('traffic_lights_failures.txt','r') as f:

	lines = f.readlines()
	for elements in lines:
		data = {}
		elements.split(',')
		var_x = elements.find("}, ")
		elements = elements[var_x:]
		data['stream_type'] = 'Twitter'
		data['text'] = re.search('"text": "(.+?)\", "created_at', elements).group(1)
		data['id_str'] = re.search('"id_str": "(.+?)\", "timestamp_ms', elements).group(1)
		print data  
