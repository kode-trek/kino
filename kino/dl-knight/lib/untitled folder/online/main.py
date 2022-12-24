from sys import argv
from shutil import move
from shutil import rmtree
from os import chdir
from os import system as s

from jl2csv import jl2csv
from mk_dl_lst import mk_dl_lst
from prs import prs

try:		rmtree('spider_1')
except:	pass

try:		s('laboratory scrapy startproject spider_1')
except:	pass

try:		tag = argv[2].split('=')[1]
except:	tag = 'body'

prs(argv[1], tag)

try:		chdir('spider_1')
except:	pass

try:		s('laboratory scrapy crawl asset -o asset.jl')
except:	pass

try:		move('asset.jl', '..')
except:	pass

try:		chdir('..')
except:	pass

try:		rmtree('spider_1')
except:	pass

jl2csv()

mk_dl_lst(argv[1])
