import collections
import queue
import random
import argparse
SEARCH_DURATION=5
TRIP_DURATION=20
DEFAULT_END_TIME=200
DEPARTURE_INTERVAL=5
DEFAULT_NUMBER_OF_TAXIS=3

Event=collections.namedtuple('Event','time ident action')

def taxi_process(ident,trips,starttime=0):

	time = yield Event(starttime,ident,'leave garange')
	for i in range(trips):
		time = yield Event(time,ident,'pick up passenger')
		time = yield Event(time,ident,'drop off passenger')
	time = yield Event(time,ident,'going home')

class Simulator:

	def __init__(self,procs_map):
		self.events = queue.PriorityQueue()
		self.procs = dict(procs_map)

	def run(self,end_time):
		'''调度并显示事件，直到时间结束'''
		for _,proc in self.procs.items():
			first_event=next(proc)
			self.events.put(first_event)
		#仿真主循环
		sim_time=0
		while sim_time < end_time:
			if self.events.empty():
				print('*** end of event***')
				break
			current_event=self.events.get()#current_event是一个Event()的namedtuple
			sim_time,proc_id,previous_action=current_event
			print('taxi:',proc_id,proc_id*' ',current_event)
			active_proc=self.procs[proc_id]
			next_time=sim_time+compute_duration(previous_action)
			try:
				next_event=active_proc.send(next_time)
			except StopIteration:
				del self.procs[proc_id]
			else:
				self.events.put(next_event)
		else:
			msg='*** end of simulation time:{} events pending ***'
			print(msg.format(self.events.qsize()))
#end taxi_simulator

def compute_duration(previous_action):
	'''使用指数分布计算操作的耗时'''
	if previous_action in ['leave garange','drop off passenger']:
		interval=SEARCH_DURATION
	elif previous_action =='pick up passenger':
		interval=TRIP_DURATION
	elif previous_action =='going home':
		interval= 1
	else:
		raise ValueError('Unknown previous_action:%s'%previous_action)
	return int(random.expovariate(1/interval))+1

def main(end_time=DEFAULT_END_TIME,num_taxi=DEFAULT_NUMBER_OF_TAXIS,seed=None):
	'''初始化随机生成器，构建过程，运行仿真程序'''
	if seed is not None:
		random.seed(seed)
	taxis={i:taxi_process(i,(i+1)*2,i*DEPARTURE_INTERVAL) for i in range(num_taxi)}
	sim=Simulator(taxis)
	sim.run(end_time)

if __name__=='__main__':
	parser =argparse.ArgumentParser(description='Taxi fleet simulator.')
	parser.add_argument('-e','--end-time',type=int,default=DEFAULT_END_TIME,help='simulaton end time;default =%s'%DEFAULT_END_TIME)
	parser.add_argument('-t','--taxis',type=int,default=DEFAULT_NUMBER_OF_TAXIS,help='number of taxis running;default=%s'%DEFAULT_NUMBER_OF_TAXIS)
	parser.add_argument('-s','--seed',type=int,default=None,help='random generator seed(for testing)')

	args=parser.parse_args()
	main(args.end_time,args.taxis,args.seed)