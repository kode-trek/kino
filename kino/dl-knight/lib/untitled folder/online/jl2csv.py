from os import remove
import json_lines

def jl2csv():
	with open('asset.jl', 'rb') as f:
		for item in json_lines.reader(f):	v = item['anchor']

	fh = open('asset.csv', 'w')
	for i in v:	fh.write(i + '\n')
	fh.close()

	try:		remove('asset.jl')
	except:	pass
