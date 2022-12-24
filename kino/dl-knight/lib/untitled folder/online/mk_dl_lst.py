from sys import argv
from os import remove

def mk_dl_lst(arg1):
	fh = open('asset.csv')
	v1 = fh.readlines()
	fh.close()

	v2 = []
	for i in v1:	v2.append(i[:-1])
	v1 = v2

	v2 = []
	for i in v1:	v2.append("axel '" + arg1 + i + "'")
	v1 = v2

	fh = open('dl-lst.sh', 'w')
	for i in v1:	fh.write(i + '\n')
	fh.close()

	try:		remove('asset.csv')
	except:	pass
