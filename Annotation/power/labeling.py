from collections import defaultdict
import json
import re

my_dict = defaultdict(list)
classify_dict = {}

tab = '\t'
comma = ','
quotes = '\', '
space = ' '
closed_br = '\']'

for line in open('sample_test_geo.txt'):
	v = line.split(tab)[0]
	key = line.split(tab)[3]
	key = key.rstrip()
	if key!= 'None':
		if key not in my_dict:
			my_dict[key] = [v]
		else:
			my_dict.setdefault(key, []).append(v)

for items in my_dict:
	print items, my_dict[items]
