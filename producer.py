import time
import zmq
import random

def producer():
	context = zmq.Context()
	zmq_socket = context.socket(zmq.PUSH)
	zmq_socket.bind("tcp://127.0.0.1:5557")
	# Start your result manager and workers before you start your producers
	while True:
		number = random.randrange(1,2000)
		print("I produce ", number)
		work_message = { 'number' : number }
		zmq_socket.send_json(work_message)
		time.sleep(3)


producer()