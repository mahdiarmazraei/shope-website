import sched
import time

scheduler = sched.scheduler(time.time,
							time.sleep)

def print_event(name):
	print('EVENT:', time.time(), name)

print ('START:', time.time())

e_x = scheduler.enterabs(time.time()+1, 1,
						print_event,
						argument = ("Event X", ));

scheduler.run()
