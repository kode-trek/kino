import os

os.system('clear')
os.system('mkdir dir1')

c = 1900
while(c <= 2020):
	os.system(
	'curl -s ' + 'http://mc4.dl3enter.in/files/Movie/' + str(c) + \
	'/ > ' + 'dir1/' + str(c)
	)
	print str(c)
	c += 1
