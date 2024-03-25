import os
import re

os.system('clear')
os.system('mkdir dir2')

c = 1900
while(c <= 2020):
	os.system('cat dir1/' + str(c) + ' > stage1')
#v1 = file-handler
	v1 = open('stage1')
#v2 = source
	v2 = v1.read()
	v1.close()
#v3 = pattern
	v3 = r'</table>'
	v4 = re.compile(v3, re.I | re.S | re.L)
#v5 = match
	v5 = v4.search(v2)

	if v5:
		os.system('cp stage1 dir2/' + str(c))
	else:
		pass
	
	c += 1

os.system('rm -r dir1; rm stage1')

del c, v1, v2, v3, v4, v5
