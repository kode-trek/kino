	sudo laboratory scrapy crawl asset -o $loc/asset.jl
	sudo rm -rf /var/www/html/q.htm /var/www/html/spider_1/

	cd $loc
	sudo chown $USER asset.jl

	laboratory python LIB/jl2csv.py
	rm asset.jl

	clear
fi
