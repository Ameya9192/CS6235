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


for line in open('crudeLabels.txt'):
	number_of_commas = line.count(comma)
	weight = line.split(closed_br)[1]
	weight = weight.strip()
	line = line.split(closed_br)[0]
	line = line.rstrip()
	if space in line:
		first_space = len(line) - len(line.lstrip())
		line_x = line.split(space)[first_space]
	i = 0
	while i <= number_of_commas:
		strip_tweet = line[12:]
		tweet = strip_tweet.split(quotes)[i]
		if tweet[0] == '\'':
			tweet = tweet[1:line.rfind('\'')]
			if weight == '1':
				print tweet + tab + 'relevant'
			else:
				print tweet + tab + 'irrelevant'

		else:
			if weight == '1': 
				print tweet + tab + 'relevant'
			else:
				print tweet + tab + 'irrelevant'
		i = i+1
