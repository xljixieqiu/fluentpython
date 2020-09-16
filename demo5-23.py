from operator import itemgetter
metro_data=[('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR','IN',21.935,(28.613889,77208889)),
('Mexico City','MX',28.142,(19.433333-99.13333)),
( 'New York- Newark','US',20.104,(48.80861,-74.920386)),
('Sao Paulo','BR',19.649,(-23.547778,-46,635833)),]
for city in sorted(metro_data,key=itemgetter(1)):
	print(city)
#与上面for循环差不多，就是没有按第一个国家简写排序
for city in metro_data:
	print(itemgetter(1)(city))
cc_name=itemgetter(1,0)
for city in metro_data:
	print(cc_name(city))
