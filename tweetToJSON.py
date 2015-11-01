import json

with open('output.txt','r') as f:
	lines = f.readlines()

lines = [line for line in lines if len(line) > 1]
data = {}

for i in range(len(lines)):

	data = {}
	tweet = json.loads(lines[i].strip())
	if(json.loads(lines[i].strip())['lang'] == 'en'):
		data['stream_type'] = 'Twitter'
		data['id_str'] = tweet['id_str']
		data['text'] = tweet['text']
		print data
	  
