import os
import re

os.system('mkdir dir3')

os.system('ls dir2/ > list1')

#v1 = file-handler
v1 = open('list1')
#v2 = list of files
v2 = v1.readlines()
v1.close()

c = 0
while(c < len(v2)):
#v3 = file-name
	v3 = v2[c][0:4]

	v1 = open('dir2/' + str(v3))
#v4 = source
	v4 = v1.read()
	v1.close()

#v5 = pattern
	v5 = r'<tr[^>]*>'
	v6 = re.compile(v5, re.I | re.S | re.L)
#v7 = match
	v7 = v6.finditer(v4)
#v8 = start
	v8 = []
	for m1 in v7:
		v8.append(m1.span())
#v9 = stop
	v5 = r'</tr>'
	v6 = re.compile(v5, re.I | re.S | re.L)
	v7 = v6.finditer(v4)

	v9 = []
	for m2 in v7:
		v9.append(m2.span())

	v8 = v8[3][0]
	v9 = v9[-2][1]

	v4 = v4[v8:v9]

	v1 = open('dir3/' + v3, 'w')
	v1.write(v4)
	v1.close()

	c += 1

os.system('rm -r dir2')

del c, v1, v2, v3, v4, v5, v6, v7, v8, v9
