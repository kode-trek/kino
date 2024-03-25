import os
import re

#v1 = file-handler
v1 = open('list1')
#v2 = list of files
v2 = v1.readlines()
v1.close()

c = 0
while(c < len(v2)):
#v3 = file-name
	v3 = v2[c][0:4]

	v1 = open('dir3/' + str(v3))
#v4 = source
	v4 = v1.read()
	v1.close()

#v5 = pattern
	v5 = r'<a href="([^>]*)">([^<]*)</a>'

	v6 = re.compile(v5, re.I | re.S | re.L)
#v7 = match
	v7 = v6.finditer(v4)

#v8 = link
#v9 = name
	v8 = []
	v9 = []
	for m in v7:
		v8.append(m.span(1))
		v9.append(m.span(2))

	v1 = open('ds.csv', 'a')

	i = 0
	while(i < len(v8)):
		name = "";	link = ""

		name = str(v4[v8[i][0]:v8[i][1]])
		link = r'http://mc4.dl3enter.in/files/Movie/' + str(v3) + '/' + \
		str(v4[v8[i][0]:v8[i][1]])

		v1.write(str(v3) + ',\t' + name + ',\t' + link + '\n')

		i += 1

	v1.close()

	c += 1

os.system('rm list1')
os.system('rm -r dir3')
os.system('clear')
#data-set (.CSV) is ready!
