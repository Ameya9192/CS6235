import json

with open('JSON.txt','r') as f:
	lines = f.readlines()


#add filters here
filters = ['closure cancelled']

with open('JSON.txt') as oldfile, open('filteredDATA.txt', 'w') as newfile:
    for lines in oldfile:
        if not any(filt in lines.lower() for filt in filters):
            newfile.write(lines)
