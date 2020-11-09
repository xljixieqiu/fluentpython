from collections import namedtuple
Event=namedtuple('Event','time ident action')
def taxi_process(ident,trips,starttime=0):
	time= yield Event(starttime,ident,'leave garage')
	for i in range(trips):
		time = yield Event(time,ident,'pick up passenger')
		time = yield Event(time,ident,'drop off passenger')
	time = yield Event(time,ident,'going home')
'''
taxi1=taxi_process(12,2,starttime=0)
next(taxi1)
taxi1.send(_.time+7)
'''